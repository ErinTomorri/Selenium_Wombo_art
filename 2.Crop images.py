import glob
import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops


"attention: this code will paste a blue square in the middle of ur image, keep the code that is commented out to not have a blue square' 
path = "enter your path"
blue = " where ur blue image is located" 
a = glob.glob(path)

num = 0

for num in range(len(a)):

    im1 = Image.open(blue)
    im2 = Image.open(a[num])
    y = im2.height
    x = im2.width
    center1 = int ((x-65-92)/2)
    center = int ((y-165-230)/2)
    x1 = 65
    y1 = 165
    x2 = x - 92
    y2 = y - 230
    im2 = im2.crop((x1, y1, x2, y2)) 
    back_im = im2.copy()
    #back_im.paste(im1, (center1,center))#if it doesnt put it in the middle just put the middle coords in 
    back_im.save(a[num], quality=100)
    num+=1
    print (num)
