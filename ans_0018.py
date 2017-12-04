#!/usr/bin/python
#-*-coding:utf-8-*-
#read city.xls of 0015 and write to city xml

import xlrd
import json

path = '0018/city.xml'

def read(xlspath):
    workbook = xlrd.open_workbook(xlspath)
    sheet = workbook.sheet_by_index(0)
    nrows = sheet.nrows
    result = {}

    for row in range(nrows):
        nvalues = sheet.row_values(row)
        cid = nvalues[0]
        cname = nvalues[1]
        result[cid]=cname
    
    return result

def write():
    data = read('0015/city.xls')
    writehead()
    writecontent(data)
    writetail()

def writehead():
    f = open(path, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8">\n')
    f.write('<root>\n')
    f.write('<cities>\n')
    f.write('<!--\n')
    f.write('\t\t城市信息\n')
    f.write('--!>\n')
    f.close()

def writecontent(data):
    f = open(path, 'a+')
    json.dump(data, f, ensure_ascii=False, indent=4)
    f.write('\n')
    f.close()

def writetail():
    f = open(path, 'a+')
    f.write('</cities>\n')
    f.write('</root>\n')

if __name__ == '__main__':
    write()
    write()