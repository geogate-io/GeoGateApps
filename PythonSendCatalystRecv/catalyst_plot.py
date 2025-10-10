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
renderView1.ViewSize = [1672, 1688]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.5015804896495636, -2.3032439084001184, 2.9518008265289217]
renderView1.CameraViewUp = [-0.41284610801539356, 0.750768015905626, 0.5156602344467448]
renderView1.CameraViewAngle = 33.09636650868878
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
layout1.SetSize(1672, 1688)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Partitioned Dataset Reader'
atm = XMLPartitionedDatasetReader(registrationName='atm', FileName=['/Users/turuncu/Desktop/output_small/atm_000000.vtpd', '/Users/turuncu/Desktop/output_small/atm_000001.vtpd', '/Users/turuncu/Desktop/output_small/atm_000002.vtpd', '/Users/turuncu/Desktop/output_small/atm_000003.vtpd'])

# create a new 'XML PolyData Reader'
coastlines_Los_Alamosvtp = XMLPolyDataReader(registrationName='Coastlines_Los_Alamos.vtp', FileName=['../data/Coastlines_Los_Alamos.vtp'])
coastlines_Los_Alamosvtp.TimeArray = 'None'

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=atm)
annotateTimeFilter1.Format = 'Time: {time: 8.1f} s'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=atm)
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'mslp_mb'
calculator1.Function = 'air_pressure_at_sea_level/100'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from annotateTimeFilter1
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
annotateTimeFilter1Display.WindowLocation = 'Upper Center'
annotateTimeFilter1Display.Position = [0.4523229912490056, 0.9372748815165878]
annotateTimeFilter1Display.Bold = 1
annotateTimeFilter1Display.FontSize = 24

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'mslp_mb'
mslp_mbTF2D = GetTransferFunction2D('mslp_mb')
mslp_mbTF2D.ScalarRangeInitialized = 1
mslp_mbTF2D.Range = [980.0, 1025.0, 0.0, 1.0]

# get color transfer function/color map for 'mslp_mb'
mslp_mbLUT = GetColorTransferFunction('mslp_mb')
mslp_mbLUT.TransferFunction2D = mslp_mbTF2D
mslp_mbLUT.RGBPoints = [980.0, 0.267004, 0.004874, 0.329415, 980.1764899999998, 0.26851, 0.009605, 0.335427, 980.352935, 0.269944, 0.014625, 0.341379, 980.529425, 0.271305, 0.019942, 0.347269, 980.70587, 0.272594, 0.025563, 0.353093, 980.88236, 0.273809, 0.031497, 0.358853, 981.0588050000001, 0.274952, 0.037752, 0.364543, 981.235295, 0.276022, 0.044167, 0.370164, 981.411785, 0.277018, 0.050344, 0.375715, 981.5882300000001, 0.277941, 0.056324, 0.381191, 981.7647200000001, 0.278791, 0.062145, 0.386592, 981.941165, 0.279566, 0.067836, 0.391917, 982.1176549999999, 0.280267, 0.073417, 0.397163, 982.2941, 0.280894, 0.078907, 0.402329, 982.4705899999999, 0.281446, 0.08432, 0.407414, 982.64708, 0.281924, 0.089666, 0.412415, 982.823525, 0.282327, 0.094955, 0.417331, 983.0000150000001, 0.282656, 0.100196, 0.42216, 983.17646, 0.28291, 0.105393, 0.426902, 983.3529500000001, 0.283091, 0.110553, 0.431554, 983.529395, 0.283197, 0.11568, 0.436115, 983.7058849999999, 0.283229, 0.120777, 0.440584, 983.8823749999999, 0.283187, 0.125848, 0.44496, 984.05882, 0.283072, 0.130895, 0.449241, 984.23531, 0.282884, 0.13592, 0.453427, 984.411755, 0.282623, 0.140926, 0.457517, 984.588245, 0.28229, 0.145912, 0.46151, 984.76469, 0.281887, 0.150881, 0.465405, 984.94118, 0.281412, 0.155834, 0.469201, 985.117625, 0.280868, 0.160771, 0.472899, 985.2941150000001, 0.280255, 0.165693, 0.476498, 985.470605, 0.279574, 0.170599, 0.479997, 985.6470499999999, 0.278826, 0.17549, 0.483397, 985.82354, 0.278012, 0.180367, 0.486697, 985.9999849999999, 0.277134, 0.185228, 0.489898, 986.176475, 0.276194, 0.190074, 0.493001, 986.35292, 0.275191, 0.194905, 0.496005, 986.5294100000001, 0.274128, 0.199721, 0.498911, 986.7059, 0.273006, 0.20452, 0.501721, 986.8823450000001, 0.271828, 0.209303, 0.504434, 987.058835, 0.270595, 0.214069, 0.507052, 987.2352799999999, 0.269308, 0.218818, 0.509577, 987.4117699999999, 0.267968, 0.223549, 0.512008, 987.5882149999999, 0.26658, 0.228262, 0.514349, 987.7647049999999, 0.265145, 0.232956, 0.516599, 987.9411949999999, 0.263663, 0.237631, 0.518762, 988.11764, 0.262138, 0.242286, 0.520837, 988.29413, 0.260571, 0.246922, 0.522828, 988.470575, 0.258965, 0.251537, 0.524736, 988.647065, 0.257322, 0.25613, 0.526563, 988.8235100000002, 0.255645, 0.260703, 0.528312, 989.0, 0.253935, 0.265254, 0.529983, 989.1764899999998, 0.252194, 0.269783, 0.531579, 989.352935, 0.250425, 0.27429, 0.533103, 989.529425, 0.248629, 0.278775, 0.534556, 989.70587, 0.246811, 0.283237, 0.535941, 989.88236, 0.244972, 0.287675, 0.53726, 990.058805, 0.243113, 0.292092, 0.538516, 990.235295, 0.241237, 0.296485, 0.539709, 990.411785, 0.239346, 0.300855, 0.540844, 990.58823, 0.237441, 0.305202, 0.541921, 990.7647200000001, 0.235526, 0.309527, 0.542944, 990.941165, 0.233603, 0.313828, 0.543914, 991.1176549999999, 0.231674, 0.318106, 0.544834, 991.2941, 0.229739, 0.322361, 0.545706, 991.47059, 0.227802, 0.326594, 0.546532, 991.64708, 0.225863, 0.330805, 0.547314, 991.823525, 0.223925, 0.334994, 0.548053, 992.0000150000001, 0.221989, 0.339161, 0.548752, 992.17646, 0.220057, 0.343307, 0.549413, 992.3529500000001, 0.21813, 0.347432, 0.550038, 992.529395, 0.21621, 0.351535, 0.550627, 992.7058849999999, 0.214298, 0.355619, 0.551184, 992.882375, 0.212395, 0.359683, 0.55171, 993.05882, 0.210503, 0.363727, 0.552206, 993.23531, 0.208623, 0.367752, 0.552675, 993.411755, 0.206756, 0.371758, 0.553117, 993.588245, 0.204903, 0.375746, 0.553533, 993.7646900000001, 0.203063, 0.379716, 0.553925, 993.94118, 0.201239, 0.38367, 0.554294, 994.1176250000001, 0.19943, 0.387607, 0.554642, 994.2941150000001, 0.197636, 0.391528, 0.554969, 994.4706050000001, 0.19586, 0.395433, 0.555276, 994.6470499999999, 0.1941, 0.399323, 0.555565, 994.82354, 0.192357, 0.403199, 0.555836, 994.9999849999999, 0.190631, 0.407061, 0.556089, 995.176475, 0.188923, 0.41091, 0.556326, 995.35292, 0.187231, 0.414746, 0.556547, 995.5294100000001, 0.185556, 0.41857, 0.556753, 995.7059, 0.183898, 0.422383, 0.556944, 995.8823450000001, 0.182256, 0.426184, 0.55712, 996.058835, 0.180629, 0.429975, 0.557282, 996.2352799999999, 0.179019, 0.433756, 0.55743, 996.41177, 0.177423, 0.437527, 0.557565, 996.588215, 0.175841, 0.44129, 0.557685, 996.764705, 0.174274, 0.445044, 0.557792, 996.941195, 0.172719, 0.448791, 0.557885, 997.11764, 0.171176, 0.45253, 0.557965, 997.29413, 0.169646, 0.456262, 0.55803, 997.470575, 0.168126, 0.459988, 0.558082, 997.647065, 0.166617, 0.463708, 0.558119, 997.8235100000002, 0.165117, 0.467423, 0.558141, 998.0, 0.163625, 0.471133, 0.558148, 998.1764899999998, 0.162142, 0.474838, 0.55814, 998.352935, 0.160665, 0.47854, 0.558115, 998.529425, 0.159194, 0.482237, 0.558073, 998.70587, 0.157729, 0.485932, 0.558013, 998.88236, 0.15627, 0.489624, 0.557936, 999.0588050000001, 0.154815, 0.493313, 0.55784, 999.2352950000001, 0.153364, 0.497, 0.557724, 999.4117850000001, 0.151918, 0.500685, 0.557587, 999.5882300000001, 0.150476, 0.504369, 0.55743, 999.7647200000001, 0.149039, 0.508051, 0.55725, 999.941165, 0.147607, 0.511733, 0.557049, 1000.1176549999999, 0.14618, 0.515413, 0.556823, 1000.2941, 0.144759, 0.519093, 0.556572, 1000.4705899999999, 0.143343, 0.522773, 0.556295, 1000.64708, 0.141935, 0.526453, 0.555991, 1000.823525, 0.140536, 0.530132, 0.555659, 1001.0000150000001, 0.139147, 0.533812, 0.555298, 1001.17646, 0.13777, 0.537492, 0.554906, 1001.3529500000001, 0.136408, 0.541173, 0.554483, 1001.529395, 0.135066, 0.544853, 0.554029, 1001.7058849999999, 0.133743, 0.548535, 0.553541, 1001.882375, 0.132444, 0.552216, 0.553018, 1002.05882, 0.131172, 0.555899, 0.552459, 1002.23531, 0.129933, 0.559582, 0.551864, 1002.411755, 0.128729, 0.563265, 0.551229, 1002.588245, 0.127568, 0.566949, 0.550556, 1002.76469, 0.126453, 0.570633, 0.549841, 1002.94118, 0.125394, 0.574318, 0.549086, 1003.117625, 0.124395, 0.578002, 0.548287, 1003.2941150000001, 0.123463, 0.581687, 0.547445, 1003.470605, 0.122606, 0.585371, 0.546557, 1003.6470499999999, 0.121831, 0.589055, 0.545623, 1003.82354, 0.121148, 0.592739, 0.544641, 1003.9999849999999, 0.120565, 0.596422, 0.543611, 1004.176475, 0.120092, 0.600104, 0.54253, 1004.35292, 0.119738, 0.603785, 0.5414, 1004.5294100000001, 0.119512, 0.607464, 0.540218, 1004.7059, 0.119423, 0.611141, 0.538982, 1004.8823450000001, 0.119483, 0.614817, 0.537692, 1005.058835, 0.119699, 0.61849, 0.536347, 1005.2352799999999, 0.120081, 0.622161, 0.534946, 1005.4117699999999, 0.120638, 0.625828, 0.533488, 1005.5882149999999, 0.12138, 0.629492, 0.531973, 1005.7647049999999, 0.122312, 0.633153, 0.530398, 1005.9411949999999, 0.123444, 0.636809, 0.528763, 1006.11764, 0.12478, 0.640461, 0.527068, 1006.29413, 0.126326, 0.644107, 0.525311, 1006.470575, 0.128087, 0.647749, 0.523491, 1006.647065, 0.130067, 0.651384, 0.521608, 1006.8235100000002, 0.132268, 0.655014, 0.519661, 1007.0, 0.134692, 0.658636, 0.517649, 1007.1764899999998, 0.137339, 0.662252, 0.515571, 1007.352935, 0.14021, 0.665859, 0.513427, 1007.529425, 0.143303, 0.669459, 0.511215, 1007.70587, 0.146616, 0.67305, 0.508936, 1007.88236, 0.150148, 0.676631, 0.506589, 1008.058805, 0.153894, 0.680203, 0.504172, 1008.235295, 0.157851, 0.683765, 0.501686, 1008.411785, 0.162016, 0.687316, 0.499129, 1008.58823, 0.166383, 0.690856, 0.496502, 1008.7647200000001, 0.170948, 0.694384, 0.493803, 1008.941165, 0.175707, 0.6979, 0.491033, 1009.1176549999999, 0.180653, 0.701402, 0.488189, 1009.2941, 0.185783, 0.704891, 0.485273, 1009.4705899999999, 0.19109, 0.708366, 0.482284, 1009.64708, 0.196571, 0.711827, 0.479221, 1009.823525, 0.202219, 0.715272, 0.476084, 1010.0000150000001, 0.20803, 0.718701, 0.472873, 1010.17646, 0.214, 0.722114, 0.469588, 1010.3529500000001, 0.220124, 0.725509, 0.466226, 1010.5293949999999, 0.226397, 0.728888, 0.462789, 1010.7058849999999, 0.232815, 0.732247, 0.459277, 1010.8823749999999, 0.239374, 0.735588, 0.455688, 1011.05882, 0.24607, 0.73891, 0.452024, 1011.23531, 0.252899, 0.742211, 0.448284, 1011.411755, 0.259857, 0.745492, 0.444467, 1011.588245, 0.266941, 0.748751, 0.440573, 1011.76469, 0.274149, 0.751988, 0.436601, 1011.94118, 0.281477, 0.755203, 0.432552, 1012.1176250000001, 0.288921, 0.758394, 0.428426, 1012.2941150000001, 0.296479, 0.761561, 0.424223, 1012.4706050000001, 0.304148, 0.764704, 0.419943, 1012.6470499999999, 0.311925, 0.767822, 0.415586, 1012.82354, 0.319809, 0.770914, 0.411152, 1012.9999849999999, 0.327796, 0.77398, 0.40664, 1013.176475, 0.335885, 0.777018, 0.402049, 1013.3529199999999, 0.344074, 0.780029, 0.397381, 1013.52941, 0.35236, 0.783011, 0.392636, 1013.7059, 0.360741, 0.785964, 0.387814, 1013.8823450000001, 0.369214, 0.788888, 0.382914, 1014.058835, 0.377779, 0.791781, 0.377939, 1014.2352799999999, 0.386433, 0.794644, 0.372886, 1014.41177, 0.395174, 0.797475, 0.367757, 1014.588215, 0.404001, 0.800275, 0.362552, 1014.764705, 0.412913, 0.803041, 0.357269, 1014.941195, 0.421908, 0.805774, 0.35191, 1015.11764, 0.430983, 0.808473, 0.346476, 1015.29413, 0.440137, 0.811138, 0.340967, 1015.470575, 0.449368, 0.813768, 0.335384, 1015.647065, 0.458674, 0.816363, 0.329727, 1015.8235100000002, 0.468053, 0.818921, 0.323998, 1016.0, 0.477504, 0.821444, 0.318195, 1016.1764899999998, 0.487026, 0.823929, 0.312321, 1016.352935, 0.496615, 0.826376, 0.306377, 1016.529425, 0.506271, 0.828786, 0.300362, 1016.70587, 0.515992, 0.831158, 0.294279, 1016.88236, 0.525776, 0.833491, 0.288127, 1017.0588050000001, 0.535621, 0.835785, 0.281908, 1017.2352950000001, 0.545524, 0.838039, 0.275626, 1017.4117850000001, 0.555484, 0.840254, 0.269281, 1017.5882300000001, 0.565498, 0.84243, 0.262877, 1017.7647200000001, 0.575563, 0.844566, 0.256415, 1017.941165, 0.585678, 0.846661, 0.249897, 1018.1176549999999, 0.595839, 0.848717, 0.243329, 1018.2941, 0.606045, 0.850733, 0.236712, 1018.4705899999999, 0.616293, 0.852709, 0.230052, 1018.64708, 0.626579, 0.854645, 0.223353, 1018.823525, 0.636902, 0.856542, 0.21662, 1019.0000150000001, 0.647257, 0.8584, 0.209861, 1019.17646, 0.657642, 0.860219, 0.203082, 1019.3529500000001, 0.668054, 0.861999, 0.196293, 1019.529395, 0.678489, 0.863742, 0.189503, 1019.7058849999999, 0.688944, 0.865448, 0.182725, 1019.882375, 0.699415, 0.867117, 0.175971, 1020.05882, 0.709898, 0.868751, 0.169257, 1020.2353099999999, 0.720391, 0.87035, 0.162603, 1020.411755, 0.730889, 0.871916, 0.156029, 1020.588245, 0.741388, 0.873449, 0.149561, 1020.76469, 0.751884, 0.874951, 0.143228, 1020.94118, 0.762373, 0.876424, 0.137064, 1021.117625, 0.772852, 0.877868, 0.131109, 1021.2941150000001, 0.783315, 0.879285, 0.125405, 1021.470605, 0.79376, 0.880678, 0.120005, 1021.6470499999999, 0.804182, 0.882046, 0.114965, 1021.82354, 0.814576, 0.883393, 0.110347, 1021.9999849999999, 0.82494, 0.88472, 0.106217, 1022.176475, 0.83527, 0.886029, 0.102646, 1022.3529199999999, 0.845561, 0.887322, 0.099702, 1022.5294100000001, 0.85581, 0.888601, 0.097452, 1022.7058999999999, 0.866013, 0.889868, 0.095953, 1022.8823449999998, 0.876168, 0.891125, 0.09525, 1023.058835, 0.886271, 0.892374, 0.095374, 1023.2352799999999, 0.89632, 0.893616, 0.096335, 1023.4117699999999, 0.906311, 0.894855, 0.098125, 1023.5882149999999, 0.916242, 0.896091, 0.100717, 1023.764705, 0.926106, 0.89733, 0.104071, 1023.941195, 0.935904, 0.89857, 0.108131, 1024.11764, 0.945636, 0.899815, 0.112838, 1024.29413, 0.9553, 0.901065, 0.118128, 1024.470575, 0.964894, 0.902323, 0.123941, 1024.6470649999999, 0.974417, 0.90359, 0.130215, 1024.8235100000002, 0.983868, 0.904867, 0.136897, 1025.0, 0.993248, 0.906157, 0.143936]
mslp_mbLUT.NanColor = [1.0, 0.0, 0.0]
mslp_mbLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'mslp_mb'
mslp_mbPWF = GetOpacityTransferFunction('mslp_mb')
mslp_mbPWF.Points = [980.0, 0.0, 0.5, 0.0, 1025.0, 1.0, 0.5, 0.0]
mslp_mbPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['CELLS', 'mslp_mb']
calculator1Display.LookupTable = mslp_mbLUT
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.TextureTransform = 'Transform2'
calculator1Display.OSPRayScaleArray = 'latitude'
calculator1Display.OSPRayScaleFunction = 'Piecewise Function'
calculator1Display.Assembly = 'Hierarchy'
calculator1Display.SelectedBlockSelectors = ['']
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 0.19999238461283428
calculator1Display.SelectScaleArray = 'mslp_mb'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'mslp_mb'
calculator1Display.GaussianRadius = 0.009999619230641714
calculator1Display.SetScaleArray = ['POINTS', 'latitude']
calculator1Display.ScaleTransferFunction = 'Piecewise Function'
calculator1Display.OpacityArray = ['POINTS', 'latitude']
calculator1Display.OpacityTransferFunction = 'Piecewise Function'
calculator1Display.DataAxesGrid = 'Grid Axes Representation'
calculator1Display.PolarAxes = 'Polar Axes Representation'
calculator1Display.ScalarOpacityFunction = mslp_mbPWF
calculator1Display.ScalarOpacityUnitDistance = 0.0860800881555703
calculator1Display.OpacityArrayName = ['CELLS', 'mslp_mb']
calculator1Display.SelectInputVectors = [None, '']
calculator1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [-49.2702, 0.0, 0.5, 0.0, 52.2462, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-90.5, 0.0, 0.5, 0.0, 90.5, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-90.5, 0.0, 0.5, 0.0, 90.5, 1.0, 0.5, 0.0]

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

# get color legend/bar for mslp_mbLUT in view renderView1
mslp_mbLUTColorBar = GetScalarBar(mslp_mbLUT, renderView1)
mslp_mbLUTColorBar.Orientation = 'Horizontal'
mslp_mbLUTColorBar.WindowLocation = 'Any Location'
mslp_mbLUTColorBar.Position = [0.2227063397129186, 0.01421800947867299]
mslp_mbLUTColorBar.Title = 'Mean Sea Level Pressure (mb)'
mslp_mbLUTColorBar.ComponentTitle = ''
mslp_mbLUTColorBar.ScalarBarLength = 0.5871770334928332
mslp_mbLUTColorBar.RangeLabelFormat = '%-#6.1f'

# set color bar visibility
mslp_mbLUTColorBar.Visibility = 1

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

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
pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [1672, 1688]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(pNG1)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.GlobalTrigger = 'Time Step'
options.CatalystLiveTrigger = 'Time Step'
options.ExtractsOutputDirectory = '.'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
