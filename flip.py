import sys
from PIL import Image
# define your flip function here
def flip(img):
    width, height = img.size
    print width, height
    imgdup = img.copy()
    matrix_orig = img.load()
    matrix_dup = imgdup.load()
    for x in range(0, width):
        for y in range(0, height):
            matrix_dup[x,y] = matrix_orig[width-x-1,y]
    imgdup.show()

if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")

# call your flip function here
img.show()
flip(img)

##hints
## width, height = img.size
###need width and height to iterate over the pixels of the image
##img.copy() duplicates the image
## write code as
### imgdup=img.copy() creates a new picture, flipped
##img.load() returns a two-dimensional matrix
##set matrix to be m = img.load()
##notation is m[x,y] or m[y][x]
