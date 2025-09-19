#!/bin/bash

backend="osmesa"

module purge

module use /lustre/desc1/scratch/epicufsrt/contrib/modulefiles_extra
module use /glade/work/epicufsrt/contrib/spack-stack/derecho/spack-stack-1.9.2/envs/ue-oneapi-2024.2.1/install/modulefiles/Core
module use /glade/work/epicufsrt/contrib/spack-stack/derecho/spack-stack-1.9.2/envs/ue-oneapi-2024.2.1/install/modulefiles/cray-mpich/8.1.29-3sepg3g/gcc/12.4.0

module use /glade/work/turuncu/ML/ufs/spack-stack/1.9.2/envs/pv_${backend}_intel/install/modulefiles/oneapi/2024.2.1
module use /glade/work/turuncu/ML/ufs/spack-stack/1.9.2/envs/pv_${backend}_intel/install/modulefiles/cray-mpich/8.1.29-3sepg3g/oneapi/2024.2.1

module load stack-oneapi/2024.2.1
module load stack-cray-mpich/8.1.29
module load cmake/3.27.9
module load stack-python/3.11.7
module load proj/8.1.0

if [ "${backend}" == "osmesa" ]; then
  module use /glade/work/turuncu/ML/ufs/spack-stack/1.9.2/envs/pv_${backend}_intel/install/modulefiles/gcc/12.4.0
fi

module load conduit/0.9.2
module load libcatalyst/2.0.0
module load paraview/5.13.1
module load stack-oneapi/2024.2.1

module use /glade/work/turuncu/ML/ufs/esmf_dev/modulefiles
module load esmf/8.8.0

module load py-xarray/2024.7.0
module load py-scipy/1.14.1

module li
