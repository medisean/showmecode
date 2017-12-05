#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import hashlib

def encode(str):
    return str.encode('UTF-8')

def md5(str):
    str = encode(str) # must encode
    hash_object = hashlib.md5(str).hexdigest()
    return hash_object

def sha1(str):
    str = encode(str)
    hash_object = hashlib.sha1(str).hexdigest()
    return hash_object

# OpenSSL Algorithms
def DSA(str):
    str = encode(str)
    hash_object = hashlib.new('DSA')
    hash_object.update(str)
    return hash_object.hexdigest()

if __name__ == '__main__':
    # print(hashlib.algorithms_available)
    # print(hashlib.algorithms_guaranteed)

    # md5
    print("md5 hello: " + md5("hello"))

    # sha1
    print("sha1 hello:" +sha1("hello"))

    # sha224 the same as above
    # ...

    # DSA
    print("DSA hello:" + DSA("hello"))