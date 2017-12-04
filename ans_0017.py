#!/usr/bin/python
#-*-coding:utf-8-*-
# 

import xlrd
import json

def read():
    try:
        data = xlrd.open_workbook('0014/students.xls')
        return data
    except:
        print(u'execel read failed')
        return None

def writecontent(data):
    sheet = data.sheet_by_index(0)
    result = {}
    nrows = sheet.nrows
    ncolumns = sheet.ncols
    path = '0017/students.xml'
    f = open(path, 'a+')
    
    for row in range(nrows):
        rvalus = sheet.row_values(row)
        sid = rvalus[0]
        sinfo = rvalus[1:]
        result[sid] = sinfo
        # f.write(json.dumps(result))

    print(json.dumps(result))
    path = '0017/students.xml'
    f = open(path, 'a+')
    json.dump(result, f, ensure_ascii=False, indent=4)
    f.write('\n')
    f.close()

def write(data):
    writehead()
    writecontent(data)
    writetail()
    

def writehead():
    path = '0017/students.xml'
    f = open(path, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<root>\n')
    f.write('<students>\n')
    f.write('<!--\n')
    f.write('       学生信息表\n')
    f.write('       "id": [名字， 数学，语文，英文]\n')
    f.write('-->\n')
    f.close()

def writetail():
    path = '0017/students.xml'
    f = open(path, 'a+')
    f.write('</students>\n')
    f.write('</root>\n')
    f.close()

if __name__ == '__main__':
    data = read()
    write(data)