#!/usr/bin/python
#-*-coding:utf-8-*-
#generate words picture validation with python

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

bgcolor = (43, 34, 88)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def generate_words(length):
	words = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
	result = ''
	for i in range(0, length):
		index = random.randint(0, 25)
		word = words[index]
		result += word
	return result

def generate_picture():
    words = generate_words(4)
    width, height = (80, 30)
    image = Image.new('RGBA', (80, 30), bgcolor)
    font_path = '/Library/Fonts/Arial.ttf'
    font = ImageFont.truetype(font_path, 25)
    draw = ImageDraw.Draw(image)

    for index in range(len(words)):
        word = words[index]
        x = index * 20 + 2
        fontcolor = generate_random_color()
        font_width, font_height = font.getsize(word)
        draw.text((x, 0), word, font = font, fill = fontcolor)

    # image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    # image = image.filter(ImageFilter.BLUR) #模糊
    image.save('0010/code.png')

if __name__ == '__main__':
    generate_picture()
