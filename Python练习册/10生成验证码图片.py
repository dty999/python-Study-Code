import random
import string
from PIL import Image, ImageDraw,ImageFont,ImageFilter

def rndChar():
    return chr(random.randint(65,91))

def getcolor1():
    return (random.randint(127,255),random.randint(127,255),random.randint(127,255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60*4
height = 60

im = Image.new("RGB", (width, height), "white")

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 36)

for i in range(width):
    for j in range(height):
        draw.point((i,j),fill=getcolor1())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

im = im.filter(ImageFilter.BLUR)
im.show()
#im.save('code.png','png')