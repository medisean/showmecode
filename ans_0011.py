#!/usr/bin/python
#-*-coding:utf-8-*-
# sensitive file filter_words.txt, when input is in the file, print Freedom, else print Human Rights

def check(word):
    file = open('0011/filtered_words.txt', 'r')
    words = file.read()
    if word in words:
        print("Freedom")
    else:
        print("Human Rights")

if __name__ == '__main__':
    while True:
        word = input('Please input a word:')
        check(word)