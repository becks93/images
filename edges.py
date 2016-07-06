#laplace program for Images project by RSS
#initializations
from filter import *

def laplace(data):
    return data[1]+data[2]+data[3]+data[4] -4*data[0]

#program start
img = open(sys.argv)
img.show()
edges = filter(img,laplace)
edges.show()