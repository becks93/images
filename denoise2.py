#condensed denoise program for Images project by RSS
#initializations
from filter import *

#returns the median value of a list of numbers
def median(data):
    data.sort()
    med_index = len(data)/2
    return data[med_index]

#program start
img = open(sys.argv)
img.show()
img = filter(img,median)
img.show()