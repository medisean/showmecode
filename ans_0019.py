#!/usr/bin/python
#-*-coding:utf-8-*-
# read number.xls of 0016 write to numbers.xml

import xlrd
import json

xmlpath = '0019/numbers.xml'

def read():
    path = '0016/numbers.xls'
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(0)
    result = []

    for row in range(sheet.nrows):
        nvalues = sheet.row_values(row)
        result.append(nvalues)
    return result

def write():
    writehead()
    writecontent()
    writetail()

def writehead():
    f = open(xmlpath, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<root>\n')
    f.write('<numbers>\n')
    f.write('<!--\n')
    f.write('\t\t数字信息\n')
    f.write('-->\n')
    f.close()

def writecontent():
    result = read()
    f = open(xmlpath, 'a+')
    json.dump(result, f, ensure_ascii=False, indent=4)
    f.write('\n')
    f.close()

def writetail():
    f = open(xmlpath, 'a+')
    f.write('</numbers>\n')
    f.write('</root>')
    f.close()

if __name__ == '__main__':
    write()