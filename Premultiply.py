from PIL import Image
import numpy
import os
import sys

def premultiplyAlpha(img):
    
    matrix = numpy.array(img)
    
    matrix[:,:,0] = numpy.round(matrix[:,:,0] * (matrix[:,:,3] / 255.0))
    matrix[:,:,1] = numpy.round(matrix[:,:,1] * (matrix[:,:,3] / 255.0))
    matrix[:,:,2] = numpy.round(matrix[:,:,2] * (matrix[:,:,3] / 255.0))
    return Image.fromarray(matrix)


rootdir = sys.argv[1]

for root, subdirs, files in os.walk(rootdir):
    
    for filename in files:
        src = os.path.join(root, filename)
        if src.endswith(".png"):
            img = Image.open(src).convert('RGBA')
            img2 = premultiplyAlpha(img)
            img2.save(src)
            print('\t- blended: %s' % (src))
        else:
            print('\t- skipped: %s' % (src))
