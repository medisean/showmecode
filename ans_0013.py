#!/usr/bin/python
#-*-coding:utf-8-*-
#download images from the link: http://tieba.baidu.com/p/2166231880

from urllib import request
import re

def downloadimages(link):
    link = 'http://tieba.baidu.com/p/2166231880'
    response = request.urlopen(link)
    html = response.read()
    html = html.decode('utf-8')

    reg = r'src="(http://img.*?\.jpg)"'
    imagelist = re.findall(reg, html)
    x = 0
    for imgurl in imagelist:
        request.urlretrieve(imgurl, '0013/%s.jpg' % x)
        x += 1

if __name__ == '__main__':
    link = 'http://tieba.baidu.com/p/2166231880'
    downloadimages(link)
    print('download success!')