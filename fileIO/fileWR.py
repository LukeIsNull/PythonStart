#!/usr/bin/env python3
#coding:utf-8

from pathlib import Path

CURRENT_PATH = Path.cwd()

def openFile():
    filePath = CURRENT_PATH / 'fileIO' / 'file.txt'
    try:
        f = open(filePath, 'r')
        print(f.read())
    finally:
        f.close()

def openFile2():
    filePath = CURRENT_PATH / 'fileIO' / 'file.txt'
    with open(filePath, 'r') as f:
        print(f.read())

def readFile():
    filePath = CURRENT_PATH / 'fileIO' / 'file.txt'
    with open(filePath, 'r') as f:
        lineNum = 1
        for line in f.readlines():
            print(f'line {lineNum} :' + line.strip())
            lineNum += 1

def writeFile():
    filePath = CURRENT_PATH / 'fileIO' / 'file.txt'
    with open(filePath, 'a') as f:
        f.write("Don't give up! \n")

def testFileWR():
    openFile()

    openFile2()

    readFile()

    # 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
    # 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
    writeFile()

    openFile2()
