#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('Helvetica', 48)

def createImage(i):
    txt = Image.new('RGBA', (64, 64), (127, 127, 127))
    d = ImageDraw.Draw(txt)
    d.text((8, 8), str(i), font=font)
    txt.save('{}.png'.format(i))

for i in range(32):
    createImage(i)
