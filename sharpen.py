#sharpen program for Images project by RSS
#initializations
from filter import *

def laplace(data):
    return data[1]+data[2]+data[3]+data[4] -4*data[0]

#returns new image based on the edges of the original
def minus(img1, img2):
    width, height = img.size
    imgnew = img1.copy()
    pixels1 = imgnew.load()
    pixels2 = img2.load()
    for x in range(0, width):
        for y in range(0, height):
            pixels1[x,y] = pixels1[x, y] - pixels2[x,y]
    return imgnew

#program start
img = open(sys.argv)
img.show()
edges = filter(img,laplace)
imgnew=minus(img,edges)
imgnew.show()
