import numpy
from mayavi.mlab import *
from mayavi import mlab


mlab.figure(1, bgcolor=(0.48, 0.48, 0.48), fgcolor=(0, 0, 0),
               size=(400, 400))
mlab.clf()

###############################################################################
# Display continents outline, using the VTK Builtin surface 'Earth'
from mayavi.sources.builtin_surface import BuiltinSurface
continents_src = BuiltinSurface(source='earth', name='Continents')
# The on_ratio of the Earth source controls the level of detail of the
# continents outline.
continents_src.data_source.on_ratio = 2
continents = mlab.pipeline.surface(continents_src, color=(0, 0, 0))

data=open("./B--1900-1905.txt")
init_flag = 0
datadict=[[0 for col in range(361)] for row in range(181)]

for line in data:
    if init_flag == 0:
        init_flag = 1
	continue
    else:
        temp = line.split()
	datadict[int(float(temp[1]))-1][int(float(temp[0]))-1] = float(temp[2])

for i in range(181):
    datadict[i][360] = datadict[i][0]

def deg2rad(ang):
    return ang*numpy.pi/180.0

def fetchdata(pos):
    return datadict[tuple(pos)]

def test_mesh():
    """A very pretty picture of spherical harmonics translated from
    the octaviz example."""
    pi = numpy.pi
    cos = numpy.cos
    sin = numpy.sin
    array, [phi,theta] = numpy.mgrid[1:181:1,1:361:1], numpy.mgrid[0:181:1,0:361:1]

    #m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
    #r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
    r = 1
    #c = numpy.asmatrix(array)
    
    phi = deg2rad(phi)
    theta = deg2rad(theta)
    x = r*sin(phi)*cos(theta)
    y = r*cos(phi)
    z = r*sin(phi)*sin(theta);
    return mesh(x, z, y, scalars=datadict)


face=test_mesh()
face.enable_contours = True
face.contour.filled_contours = True
face.contour.number_of_contours = 30

mlab.show()
