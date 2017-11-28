#!/usr/bin/python
#-*-coding:utf-8-*-
#relplace words as * when it appeared in filter_words.txt

import re

def replace(line):
    f = open('0011/filtered_words.txt', 'r')
    words = []
    for word in f:
        words.append(word.replace('\n', ''))

    for word in words:
        line = re.sub(word, "*"*len(word), line)
    return line

if __name__ == '__main__':
    while True:
        words = input("Please input a line:")
        line = replace(words)
        print(line)