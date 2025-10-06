## PythonSendCatalystReceive

This directory includes various files to define a very simple two-component coupled configuration driven by the ESMX generic driver to demonstrate the capability of [GeoGate](https://github.com/geogate-io/GeoGate) co-processing to interact with AI/ML workflows.

The configuration includes multiple instances of the GeoGate generic model component to define the coupled modeling configuration:

- **ATM:** GeoGate as a provider component

In this case, GeoGate is configured as a data component that uses a Python plugin to trigger [fake data](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/data_fake.py) or [GraphCast AI/ML workflow](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/data_graphcast.py) Python scripts.

- **COP:** GeoGate as a consumer component

The COP component is configured as a co-processing component that uses the ParaView Catalyst plugin to [write data](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/catalyst_grid_writer.py) provided by the ATM component to the disk and create simple visualizations using the visualization pipeline.

The basic configuration of the two-component modeling system can be seen in the following figure:

<img width="668" height="465" alt="Fig01" src="https://github.com/user-attachments/assets/6021c2ee-8f68-4fe6-929e-726a7022bd87" />

### Installing Dependencies

The software dependencies to run the prototype application can be installed using [Conda](https://conda-forge.org) and [Spack](https://spack.io) package managers. The dependencies are already installed on [NCAR's Derecho](https://ncar-hpc-docs.readthedocs.io/en/latest/compute-systems/derecho/) HPC platform and can be accessed in the `/glade/work/turuncu/ML/envs/spack-1.0.2/var/spack/environments/myenv` directory.

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
$ conda install -c conda-forge mpi4py mpich
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
$ cp 

$ spack concretize --force
# We need to use build_jobs=3 for LLVM to pass the build issue
$ spack install -j 3 llvm@20.1.8


spack module lmod refresh
```

If all the steps are successfully completed, the prototype application can be installed and run.

### Building and Running
