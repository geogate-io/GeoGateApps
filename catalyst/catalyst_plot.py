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
renderView1.CameraPosition = [5.551115123125783e-17, 0.0, 4.570815128681416]
renderView1.CameraFocalPoint = [5.551115123125783e-17, 0.0, 0.0]
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
atm = XMLPartitionedDatasetReader(registrationName='atm', FileName=['/Users/turuncu/Desktop/atm_000071.vtpd'])

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=atm)
annotateTimeFilter1.Format = 'Time: {time:f} sec'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from atm
atmDisplay = Show(atm, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'sea_surface_temperature'
sea_surface_temperatureTF2D = GetTransferFunction2D('sea_surface_temperature')

# get color transfer function/color map for 'sea_surface_temperature'
sea_surface_temperatureLUT = GetColorTransferFunction('sea_surface_temperature')
sea_surface_temperatureLUT.TransferFunction2D = sea_surface_temperatureTF2D
sea_surface_temperatureLUT.RGBPoints = [-0.9990535322103237, 0.231373, 0.298039, 0.752941, -5.426418203668959e-10, 0.865003, 0.865003, 0.865003, 0.99905353112504, 0.705882, 0.0156863, 0.14902]
sea_surface_temperatureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sea_surface_temperature'
sea_surface_temperaturePWF = GetOpacityTransferFunction('sea_surface_temperature')
sea_surface_temperaturePWF.Points = [-0.9990535322103237, 0.0, 0.5, 0.0, 0.99905353112504, 1.0, 0.5, 0.0]
sea_surface_temperaturePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
atmDisplay.Representation = 'Surface'
atmDisplay.ColorArrayName = ['CELLS', 'sea_surface_temperature']
atmDisplay.LookupTable = sea_surface_temperatureLUT
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
atmDisplay.ScalarOpacityFunction = sea_surface_temperaturePWF
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

# show data from annotateTimeFilter1
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
annotateTimeFilter1Display.WindowLocation = 'Any Location'
annotateTimeFilter1Display.Position = [0.4148295454545455, 0.9366130884041332]

# setup the color legend parameters for each legend in this view

# get color legend/bar for sea_surface_temperatureLUT in view renderView1
sea_surface_temperatureLUTColorBar = GetScalarBar(sea_surface_temperatureLUT, renderView1)
sea_surface_temperatureLUTColorBar.Title = 'sea_surface_temperature'
sea_surface_temperatureLUTColorBar.ComponentTitle = ''

# set color bar visibility
sea_surface_temperatureLUTColorBar.Visibility = 1

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
animationScene1.AnimationTime = 255600.0
animationScene1.StartTime = 255600.0
animationScene1.EndTime = 511200.0

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'Time Step'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [2816, 1742]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(annotateTimeFilter1)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.ExtractsOutputDirectory = '.'
options.GlobalTrigger = 'Time Step'
options.CatalystLiveTrigger = 'Time Step'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
