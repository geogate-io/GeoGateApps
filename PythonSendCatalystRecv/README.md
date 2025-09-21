## PythonSendCatalystReceive

This directory includes various files to define a very simple two component coupled configuration driven by ESMX generic driver to demostrate the capability of GeoGate to interact with AI/ML workflows.

The configuration includes multi-instance of GeoGate generic model component to define coupled modeling configuration:

- **ATM:** GeoGate as a provider component

  In this case, GeoGate configured as a data component that uses Python plugin to trigger [fake data](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/data_fake.py) or [graphcast AI/ML workflow](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/data_graphcast.py) Python scripts.

- **COP:** GeoGate as a consumer component

  The COP component configured as a co-processing component that uses ParaView Catalyst plugin to [write data](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/catalyst_grid_writer.py) provided by the ATM component to the disk and create simple visualizations using visualiation pipeline ().

The basic configuration of the two component modeling system can be see in the following figure:

<img width="704" height="394" alt="PythonSendCatalystRecv" src="https://github.com/user-attachments/assets/de9e8138-b7a9-4986-bf5c-656c82e46316" />

### Installing Dependencies

The currently tested and pre-configured work environment is available on NCAR's Derecho platform and details can be seen in the [env_derecho_intel.sh](https://github.com/geogate-io/GeoGateApps/blob/main/envs/env_derecho_intel.sh) file. The exiting environment leverages from previously installed [spack-stack](https://github.com/JCSDA/spack-stack) environment for Unified Forecast System Weather Model ([UFS-WM](https://github.com/ufs-community/ufs-weather-model)) and extends it by chaining the environment.

The similar work environment can be created by using [Spack package manager](https://spack.io). Following commands can be used as an example to setup work environment.

To install core dependencies (Ubuntu):


To create new Spack environment (pv_osmesa_gnu):

```console
foo@bar:~$ git clone --depth=2 -b v1.0.2 https://github.com/spack/spack.git spack-1.0.2
foo@bar:~$ cd spack-1.0.2
foo@bar:~$ . share/spack/setup-env.sh
foo@bar:~$ spack env create pv_osmesa_gnu
foo@bar:~$ spack env activate pv_osmesa_gnu
foo@bar:~$ cd var/spack/environments/pv_osmesa_gnu
```

To add available compilers and external packages:

```console
foo@bar:~$ spack compiler find
foo@bar:~$ spack external find --exclude cmake
```

Fınally, installing required libraries and tools:

```console
```

### Building and Running
