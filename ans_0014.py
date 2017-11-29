#!/usr/bin/python
#-*-coding:utf-8-*-
# read file of json, write to xml file

import json
import xlwt

def read(filename):
    f = open(filename, 'r')
    data = json.load(f)
    return data

def writeToExcel(lines):
    titles = ['学号', '姓名', '语文成绩', '数学成绩', '英语成绩']
    book = xlwt.Workbook()
    sheet = book.add_sheet("Sheet1")

    for i in range(len(titles)):
        sheet.write(0, i, titles[i])

    for line in lines:
        sheet.write(int(line), 0, line)
        for i in range(len(lines[line])):
            sheet.write(int(line), i+1, lines[line][i])
    book.save('0014/students.xls')

if __name__ == '__main__':
    filename = '0014/students.txt'
    data = read(filename)
    writeToExcel(data)