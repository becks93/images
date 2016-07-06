#laplace program for Images project by RSS
#initializations
from filter import *


#program start
img = open(sys.argv)
img.show()
img = filter(img,laplace)
img.show()