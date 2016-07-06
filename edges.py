#laplace program for Images project by RSS
#initializations
from filter import *

def laplace(img):
    surrounding = region3x3(img,x,y)
    return sum(surrounding[4, 1] -4*surrounding[0]

#program start
img = open(sys.argv)
img.show()
edges = filter(img,laplace)
edges.show()