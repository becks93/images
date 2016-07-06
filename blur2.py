#condensed blur program for Images project by RSS
#initializations
from filter import *

#returns the average value of a list of numbers
def avg(data):
    return sum(data)/len(data)

#program start
img = open(sys.argv)
img.show()
img = filter(img,avg)
img.show()