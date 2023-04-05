#!/usr/bin/env python3
#coding:utf-8

# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 把变量内容从序列化的对象重新读到内存里称之为反序列化

import pickle
import json

from pathlib import Path

CURRENT_PATH = Path.cwd()

def writeBytesIntoFile():
    filePath = CURRENT_PATH / 'fileIO' / 'file.txt'
    with open(filePath, 'wb') as f:
       d = dict(name = 'Bob', age = 20, score = 88)
       pickle.dump(d, f)

def loadBytesFromFile():
    filePath = CURRENT_PATH / 'fileIO' / 'file.txt'
    with open(filePath, 'rb') as f:
        d = pickle.load(f)
        print(d)

def testSerialize():
    # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
    d = dict(name = 'Bob', age = 20, score = 88)
    print(pickle.dumps(d))

    # 用pickle.dump()直接把对象序列化后写入一个file-like Object
    writeBytesIntoFile()

    # 把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
    # 或者可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
    loadBytesFromFile()
    
    # JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输
    print(json.dumps(d))

    # 默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
    # dumps()方法还提供了一大堆的可选参数,让我们来定制JSON序列化
