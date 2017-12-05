import os
from PIL import Image



def resizeImage(fileName, maxWidth, maxHeight):
	img = Image.open(fileName)
	width = img.width
	height = img.height

	if width > maxWidth and height > maxHeight:
		realHeight = int(maxWidth * height / width)
		img = img.resize((maxWidth, realHeight))
		img.save(fileName)
		resizeImage(fileName)
	elif width > maxWidth:
		realHeight = int(maxWidth * height / width)
		img = img.resize((maxWidth, realHeight))
		img.save(fileName)
	elif height > maxHeight:
		realWidth = int(maxHeight * width / height)
		img = img.resize((realWidth, maxHeight))
		img.save(fileName)
	else:
		print(str(width))

if __name__ == '__main__':
	path = '0005'
	iphone5Width = 640
	iphon5Height = 1136
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith('jpg') or file.endswith('jpeg') or file.endswith('gif') or file.endswith('png') or file.endswith('bmp'):
				filepath = path + '/' + file
				resizeImage(filepath, iphone5Width, iphon5Height)
