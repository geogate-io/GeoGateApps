# script-version: 2.0
# Catalyst state generated using paraview version 5.13.0
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2514, 1688]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.7093248238671657, -3.196673743744414, 3.189093990111296]
renderView1.CameraViewUp = [-0.5912124452198286, 0.6315754184399829, 0.5015778458420507]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.7320439376202743
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.PolarGrid = 'Polar Grid Actor'
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(2514, 1688)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML PolyData Reader'
coastlines_Los_Alamosvtp = XMLPolyDataReader(registrationName='Coastlines_Los_Alamos.vtp', FileName=['../data/Coastlines_Los_Alamos.vtp'])
coastlines_Los_Alamosvtp.TimeArray = 'None'

# create a new 'XML Partitioned Dataset Reader'
atm = XMLPartitionedDatasetReader(registrationName='atm', FileName=['/Users/turuncu/Desktop/output_operational/atm_000000.vtpd'])

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from atm
atmDisplay = Show(atm, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'eastward_wind_at_10m_height'
eastward_wind_at_10m_heightTF2D = GetTransferFunction2D('eastward_wind_at_10m_height')
eastward_wind_at_10m_heightTF2D.ScalarRangeInitialized = 1
eastward_wind_at_10m_heightTF2D.Range = [-15.0, 15.0, 0.0, 1.0]

# get color transfer function/color map for 'eastward_wind_at_10m_height'
eastward_wind_at_10m_heightLUT = GetColorTransferFunction('eastward_wind_at_10m_height')
eastward_wind_at_10m_heightLUT.TransferFunction2D = eastward_wind_at_10m_heightTF2D
eastward_wind_at_10m_heightLUT.RGBPoints = [-15.0, 0.101961, 0.101961, 0.101961, -13.117650000000001, 0.227451, 0.227451, 0.227451, -11.2353, 0.359939, 0.359939, 0.359939, -9.352935, 0.502653, 0.502653, 0.502653, -7.470585, 0.631373, 0.631373, 0.631373, -5.588235000000001, 0.749865, 0.749865, 0.749865, -3.7058850000000003, 0.843368, 0.843368, 0.843368, -1.8235349999999997, 0.926105, 0.926105, 0.926105, 0.058823549999999614, 0.999846, 0.997232, 0.995694, 1.9411800000000028, 0.994925, 0.908651, 0.857901, 3.823529999999998, 0.982468, 0.800692, 0.706113, 5.7058800000000005, 0.960323, 0.66782, 0.536332, 7.588230000000003, 0.894579, 0.503806, 0.399769, 9.470595, 0.81707, 0.33218, 0.281046, 11.352945000000002, 0.728489, 0.155017, 0.197386, 13.235295, 0.576932, 0.055363, 0.14925, 15.0, 0.403922, 0.0, 0.121569]
eastward_wind_at_10m_heightLUT.ColorSpace = 'Lab'
eastward_wind_at_10m_heightLUT.NanColor = [1.0, 0.0, 0.0]
eastward_wind_at_10m_heightLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'eastward_wind_at_10m_height'
eastward_wind_at_10m_heightPWF = GetOpacityTransferFunction('eastward_wind_at_10m_height')
eastward_wind_at_10m_heightPWF.Points = [-15.0, 0.0, 0.5, 0.0, 15.0, 1.0, 0.5, 0.0]
eastward_wind_at_10m_heightPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
atmDisplay.Representation = 'Surface'
atmDisplay.ColorArrayName = ['CELLS', 'eastward_wind_at_10m_height']
atmDisplay.LookupTable = eastward_wind_at_10m_heightLUT
atmDisplay.SelectNormalArray = 'None'
atmDisplay.SelectTangentArray = 'None'
atmDisplay.SelectTCoordArray = 'None'
atmDisplay.TextureTransform = 'Transform2'
atmDisplay.OSPRayScaleArray = 'latitude'
atmDisplay.OSPRayScaleFunction = 'Piecewise Function'
atmDisplay.Assembly = 'Hierarchy'
atmDisplay.SelectedBlockSelectors = ['']
atmDisplay.SelectOrientationVectors = 'None'
atmDisplay.ScaleFactor = 0.1999995240354704
atmDisplay.SelectScaleArray = 'None'
atmDisplay.GlyphType = 'Arrow'
atmDisplay.GlyphTableIndexArray = 'None'
atmDisplay.GaussianRadius = 0.009999976201773519
atmDisplay.SetScaleArray = ['POINTS', 'latitude']
atmDisplay.ScaleTransferFunction = 'Piecewise Function'
atmDisplay.OpacityArray = ['POINTS', 'latitude']
atmDisplay.OpacityTransferFunction = 'Piecewise Function'
atmDisplay.DataAxesGrid = 'Grid Axes Representation'
atmDisplay.PolarAxes = 'Polar Axes Representation'
atmDisplay.ScalarOpacityFunction = eastward_wind_at_10m_heightPWF
atmDisplay.ScalarOpacityUnitDistance = 0.03421025527233762
atmDisplay.OpacityArrayName = ['POINTS', 'latitude']
atmDisplay.SelectInputVectors = [None, '']
atmDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
atmDisplay.OSPRayScaleFunction.Points = [-49.2702, 0.0, 0.5, 0.0, 52.2462, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
atmDisplay.ScaleTransferFunction.Points = [-90.125, 0.0, 0.5, 0.0, 90.125, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
atmDisplay.OpacityTransferFunction.Points = [-90.125, 0.0, 0.5, 0.0, 90.125, 1.0, 0.5, 0.0]

# show data from coastlines_Los_Alamosvtp
coastlines_Los_AlamosvtpDisplay = Show(coastlines_Los_Alamosvtp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
coastlines_Los_AlamosvtpDisplay.Representation = 'Surface'
coastlines_Los_AlamosvtpDisplay.AmbientColor = [0.0, 0.0, 0.0]
coastlines_Los_AlamosvtpDisplay.ColorArrayName = [None, '']
coastlines_Los_AlamosvtpDisplay.DiffuseColor = [0.0, 0.0, 0.0]
coastlines_Los_AlamosvtpDisplay.LineWidth = 2.0
coastlines_Los_AlamosvtpDisplay.SelectNormalArray = 'None'
coastlines_Los_AlamosvtpDisplay.SelectTangentArray = 'None'
coastlines_Los_AlamosvtpDisplay.SelectTCoordArray = 'None'
coastlines_Los_AlamosvtpDisplay.TextureTransform = 'Transform2'
coastlines_Los_AlamosvtpDisplay.OSPRayScaleFunction = 'Piecewise Function'
coastlines_Los_AlamosvtpDisplay.Assembly = ''
coastlines_Los_AlamosvtpDisplay.SelectedBlockSelectors = ['']
coastlines_Los_AlamosvtpDisplay.SelectOrientationVectors = 'None'
coastlines_Los_AlamosvtpDisplay.ScaleFactor = 0.1991898834705353
coastlines_Los_AlamosvtpDisplay.SelectScaleArray = 'None'
coastlines_Los_AlamosvtpDisplay.GlyphType = 'Arrow'
coastlines_Los_AlamosvtpDisplay.GlyphTableIndexArray = 'None'
coastlines_Los_AlamosvtpDisplay.GaussianRadius = 0.009959494173526763
coastlines_Los_AlamosvtpDisplay.SetScaleArray = [None, '']
coastlines_Los_AlamosvtpDisplay.ScaleTransferFunction = 'Piecewise Function'
coastlines_Los_AlamosvtpDisplay.OpacityArray = [None, '']
coastlines_Los_AlamosvtpDisplay.OpacityTransferFunction = 'Piecewise Function'
coastlines_Los_AlamosvtpDisplay.DataAxesGrid = 'Grid Axes Representation'
coastlines_Los_AlamosvtpDisplay.PolarAxes = 'Polar Axes Representation'
coastlines_Los_AlamosvtpDisplay.SelectInputVectors = [None, '']
coastlines_Los_AlamosvtpDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
coastlines_Los_AlamosvtpDisplay.OSPRayScaleFunction.Points = [-49.2702, 0.0, 0.5, 0.0, 52.2462, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for eastward_wind_at_10m_heightLUT in view renderView1
eastward_wind_at_10m_heightLUTColorBar = GetScalarBar(eastward_wind_at_10m_heightLUT, renderView1)
eastward_wind_at_10m_heightLUTColorBar.Title = 'eastward_wind_at_10m_height'
eastward_wind_at_10m_heightLUTColorBar.ComponentTitle = ''

# set color bar visibility
eastward_wind_at_10m_heightLUTColorBar.Visibility = 1

# show color legend
atmDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'Time Step'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [2514, 1688]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(atm)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.GlobalTrigger = 'Time Step'
options.CatalystLiveTrigger = 'Time Step'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
