#!/bin/bash

ESMF_Scrip2Unstruct scrip.nc mesh.nc 0 ESMF
nccopy -k 5 mesh.nc mesh_cdf5.nc
