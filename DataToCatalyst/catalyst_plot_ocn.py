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
ocn = XMLPartitionedDatasetReader(registrationName='ocn', FileName=['/Users/turuncu/Desktop/test/ocn_000000.vtpd', '/Users/turuncu/Desktop/test/ocn_000001.vtpd', '/Users/turuncu/Desktop/test/ocn_000002.vtpd', '/Users/turuncu/Desktop/test/ocn_000003.vtpd'])

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=ocn)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from ocn
ocnDisplay = Show(ocn, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'sea_surface_temperature'
sea_surface_temperatureTF2D = GetTransferFunction2D('sea_surface_temperature')

# get color transfer function/color map for 'sea_surface_temperature'
sea_surface_temperatureLUT = GetColorTransferFunction('sea_surface_temperature')
sea_surface_temperatureLUT.TransferFunction2D = sea_surface_temperatureTF2D
sea_surface_temperatureLUT.RGBPoints = [260.0034152798349, 0.231373, 0.298039, 0.752941, 270.0, 0.865003, 0.865003, 0.865003, 279.9965847201651, 0.705882, 0.0156863, 0.14902]
sea_surface_temperatureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sea_surface_temperature'
sea_surface_temperaturePWF = GetOpacityTransferFunction('sea_surface_temperature')
sea_surface_temperaturePWF.Points = [260.0034152798349, 0.0, 0.5, 0.0, 279.9965847201651, 1.0, 0.5, 0.0]
sea_surface_temperaturePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
ocnDisplay.Representation = 'Surface'
ocnDisplay.ColorArrayName = ['CELLS', 'sea_surface_temperature']
ocnDisplay.LookupTable = sea_surface_temperatureLUT
ocnDisplay.SelectNormalArray = 'None'
ocnDisplay.SelectTangentArray = 'None'
ocnDisplay.SelectTCoordArray = 'None'
ocnDisplay.TextureTransform = 'Transform2'
ocnDisplay.OSPRayScaleArray = 'latitude'
ocnDisplay.OSPRayScaleFunction = 'Piecewise Function'
ocnDisplay.Assembly = 'Hierarchy'
ocnDisplay.SelectedBlockSelectors = ['']
ocnDisplay.SelectOrientationVectors = 'None'
ocnDisplay.ScaleFactor = 0.2
ocnDisplay.SelectScaleArray = 'None'
ocnDisplay.GlyphType = 'Arrow'
ocnDisplay.GlyphTableIndexArray = 'None'
ocnDisplay.GaussianRadius = 0.01
ocnDisplay.SetScaleArray = ['POINTS', 'latitude']
ocnDisplay.ScaleTransferFunction = 'Piecewise Function'
ocnDisplay.OpacityArray = ['POINTS', 'latitude']
ocnDisplay.OpacityTransferFunction = 'Piecewise Function'
ocnDisplay.DataAxesGrid = 'Grid Axes Representation'
ocnDisplay.PolarAxes = 'Polar Axes Representation'
ocnDisplay.ScalarOpacityFunction = sea_surface_temperaturePWF
ocnDisplay.ScalarOpacityUnitDistance = 0.08624467455908152
ocnDisplay.OpacityArrayName = ['POINTS', 'latitude']
ocnDisplay.SelectInputVectors = [None, '']
ocnDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
ocnDisplay.OSPRayScaleFunction.Points = [-49.2702, 0.0, 0.5, 0.0, 52.2462, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
ocnDisplay.ScaleTransferFunction.Points = [-90.0, 0.0, 0.5, 0.0, 90.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
ocnDisplay.OpacityTransferFunction.Points = [-90.0, 0.0, 0.5, 0.0, 90.0, 1.0, 0.5, 0.0]

# show data from annotateTimeFilter1
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
annotateTimeFilter1Display.WindowLocation = 'Any Location'
annotateTimeFilter1Display.Position = [0.4105681818181819, 0.9308725602755454]
annotateTimeFilter1Display.FontSize = 24

# setup the color legend parameters for each legend in this view

# get color legend/bar for sea_surface_temperatureLUT in view renderView1
sea_surface_temperatureLUTColorBar = GetScalarBar(sea_surface_temperatureLUT, renderView1)
sea_surface_temperatureLUTColorBar.WindowLocation = 'Any Location'
sea_surface_temperatureLUTColorBar.Position = [0.7791637073863634, 0.3344661308840414]
sea_surface_temperatureLUTColorBar.Title = 'SST'
sea_surface_temperatureLUTColorBar.ComponentTitle = ''
sea_surface_temperatureLUTColorBar.ScalarBarLength = 0.32999999999999985
sea_surface_temperatureLUTColorBar.RangeLabelFormat = '%-#6.1f'

# set color bar visibility
sea_surface_temperatureLUTColorBar.Visibility = 1

# show color legend
ocnDisplay.SetScalarBarVisibility(renderView1, True)

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
animationScene1.AnimationTime = 64800.0
animationScene1.EndTime = 64800.0
animationScene1.PlayMode = 'Snap To TimeSteps'

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'Time Step'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'plot_ocn_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [2816, 1742]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(ocn)
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
