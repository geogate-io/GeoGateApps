#!/bin/bash

module --force purge

module load ncarenv/23.09
module load gcc/12.2.0
module load cray-mpich/8.1.27
module load craype/2.7.31

module use -a /glade/work/turuncu/ML/envs/spack-1.0.2/var/spack/environments/myenv/install/modulefiles/Core
module use -a /glade/work/turuncu/ML/envs/spack-1.0.2/var/spack/environments/myenv/install/modulefiles/cray-mpich/8.1.27-6ikx5ff/Core

module load cmake/3.31.8
module load esmf/8.9.0
module load paraview/5.13.3
module load conduit/0.9.2
module load libcatalyst/2.0.0

PYTHON_ENV=/glade/work/turuncu/ML/envs/earth2studio
#export PYTHONPATH=$PYTHON_ENV/lib/python3.12:$PYTHONPATH
#export PYTHONPATH=$PYTHON_ENV/lib/python3.12/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$PYTHON_ENV/lib:$LD_LIBRARY_PATH

module li
