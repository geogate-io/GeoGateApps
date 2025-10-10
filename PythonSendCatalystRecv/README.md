## PythonSendCatalystReceive

This directory includes various files to define a very simple two-component coupled configuration driven by the ESMX generic driver to demonstrate the capability of [GeoGate](https://github.com/geogate-io/GeoGate) co-processing to interact with AI/ML workflows.

The configuration includes multiple instances of the GeoGate generic model component to define the coupled modeling configuration:

- **ATM:** In this case, GeoGate is configured as a provider (data) component that uses a Python plugin to trigger Python scripts to generate data. Please refer to Configurations section for more information about available data providers.

- **COP:** The COP component is configured as a consumer component that uses the ParaView Catalyst plugin to process data provided by the ATM component; (1) [output information](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/catalyst_grid_writer.py) in VTK format, and (2) create set of visualizations using the visualization pipeline defined in **HERE!!!**.

The basic configuration of the two-component modeling system can be seen in the following figure:

<img width="668" height="465" alt="Fig01" src="https://github.com/user-attachments/assets/6021c2ee-8f68-4fe6-929e-726a7022bd87" />

### Installing Dependencies

The software dependencies to run the prototype application can be installed using [Conda](https://conda-forge.org) and [Spack](https://spack.io) package managers. The dependencies are already installed on [NCAR's Derecho](https://ncar-hpc-docs.readthedocs.io/en/latest/compute-systems/derecho/) HPC platform and can be accessed in the `/glade/work/turuncu/ML/envs/spack-1.0.2/var/spack/environments/myenv` directory. This section can be skipped in case of using a pre-installed environment.

The following section includes information to install dependencies from scratch and uses NCAR's Derecho as an example:

- **Load base development environment**

```console
$ module purge 
$ module load ncarenv/23.09 
$ module load gcc/12.2.0
$ module load conda/latest
```
- **Create Conda environment (includes all the Python packages that we need)**

```console
$ conda create --prefix $PWD/earth2studio python=3.12
$ conda activate $PWD/earth2studio
$ uv pip install --system --break-system-packages "earth2studio@git+https://github.com/NVIDIA/earth2studio.git@0.9.0"
$ uv pip install --system --break-system-packages "earth2studio[all]@git+https://github.com/NVIDIA/earth2studio.git@0.9.0"
$ conda install -c conda-forge matplotlib==3.10.5
$ conda install -c conda-forge mako
$ conda install -c conda-forge flit-core
$ conda install -c conda-forge libpython-static
```

- **Create new Spack environment**

```console
$ git clone -b v1.0.2 --recursive https://github.com/spack/spack.git spack-1.0.2
$ cd spack-1.0.2
$ . share/spack/setup-env.sh
$ spack repo update builtin --commit 2ebf5115bf14e306903196861503fc630610b750
$ spack env create myenv
$ cd var/spack/environments/myenv
$ spack env activate .
```
Note: The `spack repo update builtin --commit [HASH]` command updates the [Spack packages](https://github.com/spack/spack-packages) to their more recent version that includes `esmf@8.9.0`. The Spack package recipes can be found in the `~/.spack/package_repos` directory.

- **Install dependencies using Spack package manager**

Once both the Conda and Spack environments are created and ready to use, the Spack environment can be specialized to include all the library dependencies. In this case, Python and its modules are defined as external packages (`packages_gnu.yaml` file). Note that this file was specifically created for [NCAR's Derecho](https://ncar-hpc-docs.readthedocs.io/en/latest/compute-systems/derecho/) HPC platform, but it can be used as a reference to create a similar file for other HPC platforms or local installations. In addition to the `packages_gnu.yaml` file, the `modules.yaml` file is also created to enable module file generation for installed Spack packages.

```console
$ cd var/spack/environments/myenv
$ wget https://raw.githubusercontent.com/geogate-io/GeoGateApps/refs/heads/main/envs/derecho/modules.yaml
$ wget -O packages.yaml https://raw.githubusercontent.com/geogate-io/GeoGateApps/refs/heads/main/envs/derecho/packages_gnu.yaml  
$ wget https://raw.githubusercontent.com/geogate-io/GeoGateApps/refs/heads/main/envs/derecho/spack.yaml
$ spack concretize --force
# We need to use build_jobs=3 for LLVM to pass the build issue
$ spack install -j 3 llvm@20.1.8
$ spack install
$ spack module lmod refresh
```

If all the steps are successfully completed, the prototype application can be installed and run.

### Configurations

The current version of the **PythonSendCatalystReceive** test configuration can be run with three different data sources for the ATM component: (1) fake data, (2) GraphCast Small AI model (default), and (3) GraphCast Operational AI model.

In each case, the simple configuration only exports three variables: 10-meter wind components (`u10m` and `v10m`) and mean sea level pressure (`msl`) but the GeoGate component is designed to be flexible and can be configured to pass any data provided by the Python script to other components (physical, AI/ML or co-processing).

The list of export fields are defined using `ExportFields` configuration option that can be seen in the [esmxRun.yaml](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/esmxRun.yaml) configuration file.

```
ExportFields: [eastward_wind_at_10m_height, northward_wind_at_10m_height, air_pressure_at_sea_level]
```

Note: The names of the fields need to match with the names in the Python script to ingest data correctly.

#### a. Fake Data

The [fake data](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/data_fake.py) script basicaly manuplates the export fields (initialized to 0 in the ATM component) and fill them with artifical data using the same method provided by [ESMF_FieldFill()](https://earthsystemmodeling.org/docs/release/latest/ESMF_refdoc/node5.html#SECTION050365300000000000000) call (dataFillScheme set to `sincos`).

The mesh file used for the ATM export state and the Python script that is used to manipulate the data are defined in the [esmxRun.yaml](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/esmxRun.yaml) configuration file (see the ATM/attributes section). In this case, the `PythonScripts` and `ExportMeshFile` options are set like the following:

```
PythonScripts: data_fake.py
ExportMeshFile: ../meshes/era5_mesh.nc
```

The model will output data in netCDF, binary ([Conduit](https://llnl-conduit.readthedocs.io/en/latest/) nodes), and [VTK](https://docs.paraview.org/en/latest/UsersGuide/understandingData.html) formats to check the results.

#### b. GraphCast Small (1.0 deg)

The [GraphCastSmall](https://nvidia.github.io/earth2studio/modules/generated/models/px/earth2studio.models.px.GraphCastSmall.html) model is a smaller, low-resolution version of GraphCast (1 degree resolution, 13 pressure levels and a smaller mesh), trained on ERA5 data from 1979 to 2015.

To run this configuration, the `PythonScripts` and `ExportMeshFile` options need to be set as follows in the [esmxRun.yaml](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/esmxRun.yaml) configuration file.

```
PythonScripts: data_graphcast_small.py
ExportMeshFile: ../meshes/graphcast_small_mesh_cdf5.nc
```

Note: The ESMF mesh files used in these examples are created previously using the [ proc_scrip.py](https://github.com/geogate-io/GeoGateApps/blob/main/tools/proc_scrip.py) and the [scrip2mesh.sh](https://github.com/geogate-io/GeoGateApps/blob/main/tools/scrip2mesh.sh) scripts. In case of using a new data source or data set, the user needs to create a new mesh file.

#### c. GraphCast Operational (0.25 deg)

The [GraphCastOperational](https://nvidia.github.io/earth2studio/modules/generated/models/px/earth2studio.models.px.GraphCastOperational.html#earth2studio.models.px.GraphCastOperational) model is a high-resolution model (0.25 degree resolution, 13 pressure levels) pre-trained on ERA5 data from 1979 to 2017 and fine-tuned on HRES data from 2016 to 2021. 

To run this configuration, the `PythonScripts` and `ExportMeshFile` options need to be set as follows in the [esmxRun.yaml](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/esmxRun.yaml) configuration file.

```
PythonScripts: data_graphcast_operational.py
ExportMeshFile: ../meshes/graphcast_operational_mesh_cdf5.nc
```

### Building and Running

To build the configuration, the [build.sh](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/build.sh) script can be used. The script relies on a pre-installed Spack environment and uses the [derecho_env_gnu.sh](https://github.com/geogate-io/GeoGateApps/blob/main/envs/derecho_env_gnu.sh) file to load required modules.

Once the configuration is compiled successfully, it can be run by using the job submission script (NCAR Derecho, https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/job_card.derecho).

To run GraphCast models on GPU, the job submission script can be modified to request GPU resources as follows:

```
...
#PBS -q main
#PBS -l select=1:ncpus=2:mpiprocs=2:ompthreads=1:ngpus=1
...
```

### References

The GraphCast configurations use NVIDIA's [Earth2Studio](https://nvidia.github.io/earth2studio/index.html) toolkit to run available GraphCast models ([Lam et al., 2023](https://www.science.org/doi/10.1126/science.adi2336)).
