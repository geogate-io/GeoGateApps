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
renderView1.ViewSize = [2816, 1742]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [5.551115123125783e-17, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.9986829320433575, 0.3568351992908332, 4.095153979802056]
renderView1.CameraFocalPoint = [5.551115123125782e-17, 8.596747779868897e-35, 2.6134113250801447e-33]
renderView1.CameraViewUp = [0.0040504779497368, 0.9960440806659936, -0.08876814179994097]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.7320508075688772
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.PolarGrid = 'Polar Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(2816, 1742)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Partitioned Dataset Reader'
atm = XMLPartitionedDatasetReader(registrationName='atm', FileName=['/Users/turuncu/Desktop/test/atm_000000.vtpd', '/Users/turuncu/Desktop/test/atm_000001.vtpd', '/Users/turuncu/Desktop/test/atm_000002.vtpd', '/Users/turuncu/Desktop/test/atm_000003.vtpd'])

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=atm)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from annotateTimeFilter1
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
annotateTimeFilter1Display.WindowLocation = 'Any Location'
annotateTimeFilter1Display.Position = [0.4105681818181819, 0.9308725602755454]
annotateTimeFilter1Display.FontSize = 24

# show data from atm
atmDisplay = Show(atm, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'eastward_wind_at_10m_height'
eastward_wind_at_10m_heightTF2D = GetTransferFunction2D('eastward_wind_at_10m_height')

# get color transfer function/color map for 'eastward_wind_at_10m_height'
eastward_wind_at_10m_heightLUT = GetColorTransferFunction('eastward_wind_at_10m_height')
eastward_wind_at_10m_heightLUT.TransferFunction2D = eastward_wind_at_10m_heightTF2D
eastward_wind_at_10m_heightLUT.RGBPoints = [-4.998289489676763, 0.231373, 0.298039, 0.752941, 0.0, 0.865003, 0.865003, 0.865003, 4.998289489676763, 0.705882, 0.0156863, 0.14902]
eastward_wind_at_10m_heightLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'eastward_wind_at_10m_height'
eastward_wind_at_10m_heightPWF = GetOpacityTransferFunction('eastward_wind_at_10m_height')
eastward_wind_at_10m_heightPWF.Points = [-4.998289489676763, 0.0, 0.5, 0.0, 4.998289489676763, 1.0, 0.5, 0.0]
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
atmDisplay.ScaleFactor = 0.2
atmDisplay.SelectScaleArray = 'None'
atmDisplay.GlyphType = 'Arrow'
atmDisplay.GlyphTableIndexArray = 'None'
atmDisplay.GaussianRadius = 0.01
atmDisplay.SetScaleArray = ['POINTS', 'latitude']
atmDisplay.ScaleTransferFunction = 'Piecewise Function'
atmDisplay.OpacityArray = ['POINTS', 'latitude']
atmDisplay.OpacityTransferFunction = 'Piecewise Function'
atmDisplay.DataAxesGrid = 'Grid Axes Representation'
atmDisplay.PolarAxes = 'Polar Axes Representation'
atmDisplay.ScalarOpacityFunction = eastward_wind_at_10m_heightPWF
atmDisplay.ScalarOpacityUnitDistance = 0.08624467455908152
atmDisplay.OpacityArrayName = ['POINTS', 'latitude']
atmDisplay.SelectInputVectors = [None, '']
atmDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
atmDisplay.OSPRayScaleFunction.Points = [-49.2702, 0.0, 0.5, 0.0, 52.2462, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
atmDisplay.ScaleTransferFunction.Points = [-90.0, 0.0, 0.5, 0.0, 90.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
atmDisplay.OpacityTransferFunction.Points = [-90.0, 0.0, 0.5, 0.0, 90.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for eastward_wind_at_10m_heightLUT in view renderView1
eastward_wind_at_10m_heightLUTColorBar = GetScalarBar(eastward_wind_at_10m_heightLUT, renderView1)
eastward_wind_at_10m_heightLUTColorBar.WindowLocation = 'Any Location'
eastward_wind_at_10m_heightLUTColorBar.Position = [0.7738370028409092, 0.3358208955223881]
eastward_wind_at_10m_heightLUTColorBar.Title = 'U10'
eastward_wind_at_10m_heightLUTColorBar.ComponentTitle = ''
eastward_wind_at_10m_heightLUTColorBar.ScalarBarLength = 0.3299999999999998

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

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 64800.0
animationScene1.EndTime = 64800.0
animationScene1.PlayMode = 'Snap To TimeSteps'

# initialize the animation scene

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'Time Step'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'plot_atm_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [2816, 1742]
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
