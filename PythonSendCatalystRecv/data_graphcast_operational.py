import os
import xarray as xr
from conduit import Node 
import earth2studio
from earth2studio.models.px import GraphCastOperational
from earth2studio.data import WB2ERA5
from earth2studio.io import XarrayBackend
from earth2studio.run import deterministic as run

# Arguments
state = "export"
channel = "atm"
nx_atm = 1440
nx_atm = 721
debug = True 

# Access to channel
my_channel = my_node["channels/{}/{}".format(state, channel)]

# Model specific parameters
forecast = my_node['state/time_str']
step = 1 # lead time is 6h

# Create model, dataset for input and also io object for output
package = GraphCastOperational.load_default_package()
model = GraphCastOperational.load_model(package)
ds_input = WB2ERA5(cache=True)
io = XarrayBackend()

# Run model
run([forecast], step, model, ds_input, io)

# Save results
if debug:
    io.root.to_netcdf("graphcast_operational_{}_{}_{}.nc".format(state, channel, forecast))

# Return node with data
lead_time = 1
my_node_return = Node()
my_node_return.update(my_channel)
my_node_return['data/fields/air_pressure_at_sea_level/values'] = io.root['msl'][0,lead_time].values.reshape(-1)
my_node_return['data/fields/eastward_wind_at_10m_height/values'] = io.root['u10m'][0,lead_time].values.reshape(-1)
my_node_return['data/fields/northward_wind_at_10m_height/values'] = io.root['v10m'][0,lead_time].values.reshape(-1)
if debug:
    my_node_return.save('my_node_return')
