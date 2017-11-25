#!/usr/bin/python  
#-*-coding:utf-8-*-  

# 一个HMTL文件，找出里面的正文

if __name__ == '__main__':
	filename = '0008/0008.html'
	f = open(filename, 'r')
	isStartLine = False
	isEnd = False

	for line in f:
		if isEnd:
			break

		bodyIndex = line.find('<body>')
		endBodyIndex = line.find('</body>')

		if bodyIndex != -1:
			isStartLine = True
			print(line[7:])
		elif endBodyIndex != -1:
			isEnd = True
			print(line[:endBodyIndex])
		elif isStartLine:
			print(line)

