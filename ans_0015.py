#!/usr/bin/python
#-*-coding:utf-8-*-
#write city.txt to xls

import json
import xlwt

def read(filename):
    f = open(filename, 'r')
    data = json.load(f)
    return data

def writeToXLS(lines):
    book = xlwt.Workbook()
    sheet = book.add_sheet("city")

    for line in lines:
        sheet.write(int(line)-1, 0, line)
        sheet.write(int(line)-1, 1, lines[line])
    book.save('0015/city.xls')

if __name__ == '__main__':
    data = read('0015/city.txt')
    writeToXLS(data)