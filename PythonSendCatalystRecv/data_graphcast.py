import os
import xarray as xr
import earth2studio
from earth2studio.models.px import GraphCastSmall
from earth2studio.data import WB2ERA5
from earth2studio.io import NetCDF4Backend
from earth2studio.run import deterministic as run
