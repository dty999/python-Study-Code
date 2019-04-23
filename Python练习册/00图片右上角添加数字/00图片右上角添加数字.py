import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

font = ImageFont.truetype('msyhbd.ttc',36)

imageFile = 'test.png'
im1 = Image.open(imageFile)

x, y = im1.size



draw = ImageDraw.Draw(im1)
draw.text((x/2,y/2),'2',(255,0,0),font = font)
draw = ImageDraw.Draw(im1)

im1.save('target.png')