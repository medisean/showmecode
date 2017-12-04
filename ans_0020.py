#!/usr/bin/python
#-*-coding:utf-8-*-
# read 0020/time.xls and count total time

import xlrd

def read():
    path = '0020/time.xls'
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_name('numbers')
    total = 0
    for row in range(1, sheet.nrows):
        rvalues = sheet.row_values(row)
        time = rvalues[1]
        total += counttime(time)
    
    h = int(total / 3600)
    m = int((total % 3600) / 60)
    s = int(total % 60)
    
    result = '总通话时间：'
    if h != 0:
        result += str(h) + '小时'
    if m != 0:
        result += str(m) + '分钟'
    if s != 0:
        result += str(s) + '秒'
    print(result)

def counttime(time):
    h, m, s = 0, 0, 0
    h_str = "小时"
    m_str = "分"
    s_str = "秒"
    h_index, m_index, s_index = -1, -1, -1

    if h_str in time:
        h_index = time.find(h_str)
        h = int(time[:h_index])

    if m_str in time:
        m_index = time.find(m_str)
        if h_index != -1:
            m = int(time[h_index+2:m_index])
        else:
            m = int(time[:m_index])
    
    if s_str in time:
        s_index = time.find(s_str)
        if m_index != -1:
            s = int(time[m_index+1:s_index])
        else:
            s = int(time[:s_index])
    return h * 3600 + m * 60 + s

if __name__ == '__main__':
    read()