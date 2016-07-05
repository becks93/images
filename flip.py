#flip program for Images Project by RSS
#initializations
import sys
from PIL import Image

#flips and displays an image
def flip(img):
    width, height = img.size
    imgdup = img.copy()
    matrix_orig = img.load()
    matrix_dup = imgdup.load()
    for x in range(0, width):
        for y in range(0, height):
            matrix_dup[x,y] = matrix_orig[width-x-1,y]
    imgdup.show()

#program start
if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()
flip(img)
