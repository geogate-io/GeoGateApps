## PythonSendCatalystReceive

This directory includes various files to define a very simple two component coupled configuration driven by ESMX generic driver to demostrate the capability of GeoGate to interact with AI/ML workflows.

The configuration includes multi-instance of GeoGate generic model component to define coupled modeling configuration:

- **ATM:** GeoGate as a provider component (export)

  In this case, GeoGate acts like a data component that uses Python plugin and enables to trigger [fake data](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/data_fake.py) or [graphcast AI/ML workflow](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/data_graphcast.py).

- **COP:** GeoGate as a consumer component (import)

  The COP component acts like a co-processing component that uses ParaView Catalyst plugin to [write data](https://github.com/geogate-io/GeoGateApps/blob/main/PythonSendCatalystRecv/catalyst_grid_writer.py) provided by ATM component to the disk and create simple visualizations (.

### Installing Dependencies
