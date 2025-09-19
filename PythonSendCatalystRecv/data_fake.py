import os
from conduit import Node
import numpy as np
import xarray as xr

# Arguments
state = "export"
channel = "atm"
nx_atm = 1440
ny_atm = 721
debug = False 

# Access to channel 
my_channel = my_node["channels/{}/{}".format(state, channel)]

# Save the data in the channel
if debug:
    my_channel.save('my_channel')

# Create dataset
# We need to reshape the data since it is provided in 1d for now (stored on mesh)
ds = xr.Dataset(
    data_vars = {
        "mask": (["lat", "lon"], my_channel['data/mask/values/face_mask'].reshape((ny_atm,nx_atm))),
        "slp" : (["lat", "lon"], my_channel['data/fields/air_pressure_at_sea_level/values'].reshape((ny_atm,nx_atm))),
        "u10" : (["lat", "lon"], my_channel['data/fields/eastward_wind_at_10m_height/values'].reshape((ny_atm,nx_atm))),
        "v10" : (["lat", "lon"], my_channel['data/fields/northward_wind_at_10m_height/values'].reshape((ny_atm,nx_atm)))
    },
    coords = {
        "lon": (["lat", "lon"], my_channel['data/coords/values/face_lon'].reshape((ny_atm,nx_atm))),
        "lat": (["lat", "lon"], my_channel['data/coords/values/face_lat'].reshape((ny_atm,nx_atm)))
    }
)

# Save initial dataset
if debug:
    tstr = my_node['state/time_str']
    ds.to_netcdf("{}_{}_{}_before.nc".format(state, channel, tstr))

# Modify data, same method used in ESMF_FieldFill() call using sincos argument
# Slightly modify data based on the time step to have time varying data
tstep = my_node['state/time_step']+1
member = 10.0*tstep
ds["slp"] = np.cos(member*ds["lon"]*3.1416/360.0)*np.sin(member*ds["lat"]*3.1416/360.0)
member = 5.0*tstep
ds["u10"] = np.cos(member*ds["lon"]*3.1416/360.0)*np.sin(member*ds["lat"]*3.1416/360.0)
member = 2.0*tstep
ds["v10"] = np.cos(member*ds["lon"]*3.1416/360.0)*np.sin(member*ds["lat"]*3.1416/360.0)

# Save dataset after update
if debug:
    tstr = my_node['state/time_str']
    ds.to_netcdf("{}_{}_{}_after.nc".format(state, channel, tstr))

# Return new node with modified data
my_node_return = Node()
my_node_return.update(my_channel)
my_node_return['data/fields/air_pressure_at_sea_level/values'] = ds['slp'].values.reshape(-1)
my_node_return['data/fields/eastward_wind_at_10m_height/values'] = ds['u10'].values.reshape(-1)
my_node_return['data/fields/northward_wind_at_10m_height/values'] = ds['v10'].values.reshape(-1)
