import os
import sys
import numpy as np
import xarray as xr
import argparse

def calc_corners(xc, yc, delta=0.25):
    """
    Calculate corner coordinates by averaging neighbor cells
    It follows the approach initially developed by NCL and made
    available through calc_SCRIP_corners_noboundaries() call
    """

    # Get sizes of original array
    ny, nx = xc.shape

    # Extend array that stores center coordinates
    xc_ext = np.pad(xc, ((1,1), (1,1)), constant_values=(0, 0))
    yc_ext = np.pad(yc, ((1,1), (1,1)), constant_values=(0, 0))

    # Get sizes, extended array
    ny_ext, nx_ext = xc_ext.shape

    # Fill missing part of expanded array
    # Bottom row, minus corners (left side in data)
    xc_ext[1:ny_ext-1,0] = mirrorP2P(xc[:,1], xc[:,0])
    yc_ext[1:ny_ext-1,0] = mirrorP2P(yc[:,1], yc[:,0])

    # Top, minus corners (right side in data)
    xc_ext[1:ny_ext-1,nx_ext-1] = mirrorP2P(xc[:,nx-2], xc[:,nx-1])
    yc_ext[1:ny_ext-1,nx_ext-1] = mirrorP2P(yc[:,nx-2], yc[:,nx-1])

    # Left, minus corners (top side in data)
    xc_ext[0,1:nx_ext-1] = mirrorP2P(xc[1,:], xc[0,:])
    yc_ext[0,1:nx_ext-1] = mirrorP2P(yc[1,:], yc[0,:])

    # Right, minus corners (bottom side in data)
    xc_ext[ny_ext-1,1:nx_ext-1] = mirrorP2P(xc[ny-2,:], xc[ny-1,:])
    yc_ext[ny_ext-1,1:nx_ext-1] = mirrorP2P(yc[ny-2,:], yc[ny-1,:])

    # Lower left corner (upper left corner in data)
    xc_ext[0,0] = mirrorP2P(xc[1,1], xc[0,0])
    yc_ext[0,0] = mirrorP2P(yc[1,1], yc[0,0])

    # Upper right corner (lower right corner in data)
    xc_ext[ny_ext-1,nx_ext-1] = mirrorP2P(xc[ny-2,nx-2], xc[ny-1,nx-1])
    yc_ext[ny_ext-1,nx_ext-1] = mirrorP2P(yc[ny-2,nx-2], yc[ny-1,nx-1])

    # Lower right corner (upper right corner in data)
    xc_ext[0,nx_ext-1] = mirrorP2P(xc[1,nx-2], xc[0,nx-1])
    yc_ext[0,nx_ext-1] = mirrorP2P(yc[1,nx-2], yc[0,nx-1])

    # Upper left corner (lower left corner in data)
    xc_ext[ny_ext-1,0] = mirrorP2P(xc[ny-2,1], xc[ny-1,0])
    yc_ext[ny_ext-1,0] = mirrorP2P(yc[ny-2,1], yc[ny-1,0])

    # TODO: need to add code for boundary corners if they go over

    # The cell center of the extended grid, which
    # would be the corner coordinates for the original grid
    xo = xc_ext[:,1:nx_ext]+xc_ext[:,0:nx_ext-1]
    xo = delta*(xo[1:ny_ext,:]+xo[0:ny_ext-1,:])
    yo = yc_ext[:,1:nx_ext]+yc_ext[:,0:nx_ext-1]
    yo = delta*(yo[1:ny_ext,:]+yo[0:ny_ext-1,:])

    # Create flattened version of corner coordinates
    kernel = np.array([[1,1], [1,1]])
    xo = arrays_from_kernel(xo, kernel).reshape(ny,nx,-1).reshape(-1,kernel.size)
    xo = xo[:,[0, 1, 3, 2]]
    yo = arrays_from_kernel(yo, kernel).reshape(ny,nx,-1).reshape(-1,kernel.size)
    yo = yo[:,[0, 1, 3, 2]]

    # Return flatten arrays
    return(np.ndarray.flatten(xc),
           np.ndarray.flatten(yc),
           xo,
           yo)

def mirrorP2P(p1, p0):
    """
    This functions calculates the mirror of p1 with respect to po
    """
    dVec = p1-p0
    return(p0-dVec)

def arrays_from_kernel(arr, kernel):
    windows = sliding_window(arr, kernel.shape)
    return np.where(kernel, windows, 0)

def sliding_window(data, win_shape, **kwargs):
    assert data.ndim == len(win_shape)
    shape = tuple(dn - wn + 1 for dn, wn in zip(data.shape, win_shape)) + win_shape
    strides = data.strides * 2
    return np.lib.stride_tricks.as_strided(data, shape=shape, strides=strides, **kwargs)

def to_scrip(xc, yc, xo, yo, mc, dims, output_file='scrip.nc', output_dir='./'):
    """
    Writes grid in SCRIP format
    """

    # Create new dataset in SCRIP format
    out = xr.Dataset()

    # Fill with data
    out['grid_dims'] = xr.DataArray(np.array(dims, dtype=np.int32), dims=('grid_rank',))
    out['grid_center_lon'] = xr.DataArray(xc, dims=('grid_size'), attrs={'units': 'degrees'})
    out['grid_center_lat'] = xr.DataArray(yc, dims=('grid_size'), attrs={'units': 'degrees'})
    out['grid_corner_lon'] = xr.DataArray(xo, dims=('grid_size','grid_corners'), attrs={'units': 'degrees'}).astype(dtype=np.float64, order='F')
    out['grid_corner_lat'] = xr.DataArray(yo, dims=('grid_size','grid_corners'), attrs={'units': 'degrees'}).astype(dtype=np.float64, order='F')
    out['grid_imask'] = xr.DataArray(mc, dims=('grid_size'), attrs={'units': 'unitless'})
    out['grid_area'] = xr.DataArray(mc, dims=('grid_size'), attrs={'units': 'unitless'})
   
    # Force no '_FillValue' if not specified
    for v in out.variables:
        if '_FillValue' not in out[v].encoding:
            out[v].encoding['_FillValue'] = None    

    # Add global attributes
    out.attrs = {'title': 'Grid with {} size'.format('x'.join(list(map(str,dims)))),
                 'conventions': 'SCRIP'}

    # Write dataset
    ofile = os.path.join(output_dir, output_file)
    out.to_netcdf(ofile, engine="netcdf4")

    return(ofile)

def main(argv):
    """
    Main function to create SCRIP grid definition file
    """
    # Parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--ifile'  , help='Input file name' , required=True)
    args = parser.parse_args()

    if args.ifile:
        input_file = args.ifile

    # Print out configuration
    print("Configuration:")
    print("ifile = {}".format(input_file))

    # Open file
    ds = xr.open_dataset(input_file)

    # Get coordinate information
    nx = ds['lon'].size
    ny = ds['lat'].size
    lon2d = ds['lon'].expand_dims(dim={'y': ny}).to_numpy()
    lat2d = ds['lat'].expand_dims(dim={'x': nx}).transpose().to_numpy()

    # Create SCRIP file
    xc, yc, xo, yo = calc_corners(lon2d, lat2d)
    to_scrip(xc, yc, xo, yo, np.ones(xc.size, dtype=np.int32), xc.shape[::-1], output_dir='./')

if __name__== "__main__":
    main(sys.argv[1:])
