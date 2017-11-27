#!/usr/bin/python
#-*-coding:utf-8-**

#一个HTML文件，找出里面的链接

import re

def findLink(file):
    file_object = open(file)
    try:
        all_the_text = file_object.read()
        pattern = r'<[aA].*?/[aA]>'
        allResults = re.findall(pattern, all_the_text)
        for result in allResults:
            print(result)
    finally:
        file_object.close( )

if __name__ == '__main__':
	findLink('0009/9.html')