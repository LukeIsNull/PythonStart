#!/usr/bin/env python3
#coding:utf-8

import os

def testFileAndDir():
    print(os.name)
    print(os.uname())

    #环境变量
    print(os.environ)

    # 查看当前目录的绝对路径
    print(os.path.abspath('.'))

    # 拼接路径
    os.path.join('/Users/lukezhou/Study/Code/PythonStart', 'testDir')
    # 拆分路径
    os.path.split('/Users/lukezhou/Study/Code/PythonStart/fileIO/fileAndDir.py')

    # 创建一个目录
    os.mkdir('/Users/lukezhou/Study/Code/PythonStart/testDir')
    # 删除一个目录
    os.rmdir('/Users/lukezhou/Study/Code/PythonStart/testDir')
