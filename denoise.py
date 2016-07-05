#denoise program for Images Project by RSS
#initializations
import sys
from PIL import Image

#removes some noise from blurry picture and displays new version
def denoise(img):
    width, height = img.size
    imgdup = img.copy()
    pixels = imgdup.load()
    for x in range(0, width):
        for y in range(0, height):
            r=region3x3(img,x,y)
            pixels[x,y]=median(r)
    imgdup.show()

#returns the median value of a list of numbers
def median(data):
    data.sort()
    med_index = len(data)/2
    return data[med_index]

#defines a pixel region surrounding a specific point
def region3x3(img,x,y):
    me =getpixel(img,x,y)
    N=getpixel(img,x,y-1)
    S=getpixel(img,x,y+1)
    E=getpixel(img,x+1,y)
    W=getpixel(img,x-1,y)
    NW=getpixel(img,x-1,y-1)
    NE=getpixel(img,x+1,y-1)
    SE=getpixel(img,x+1,y+1)
    SW=getpixel(img,x-1,y+1)
    return [me,N,S,E,W,NW,NE,SE,SW]

#returns a specific pixel
def getpixel(img,x,y):
    width,height=img.size
    if x<0:
        x=0
    elif x>=width:
        x=width-1
    if y<0:
        y=0
    elif y>=height:
        y=height-1
    return img.load()[x,y]

#program start
if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()
denoise(img)
