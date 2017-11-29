#!/usr/bin/python
#-*-coding:utf-8-*-
# read numbers.txt and write to number.xls

import json
import xlwt

def read(filename):
    f = open(filename, 'r')
    data = json.load(f)
    return data

def write(data):
    book = xlwt.Workbook()
    sheet = book.add_sheet('numbers')

    x = 0
    for line in data:
        y = 0
        for number in line:
            sheet.write(x, y, line[y])
            y += 1
        x += 1
    book.save('0016/numbers.xls')

if __name__ == '__main__':
    data = read('0016/numbers.txt')
    write(data)
    