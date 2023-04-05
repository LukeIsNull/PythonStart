#!/usr/bin/env python3
#coding:utf-8

# 匿名函数不会有名字冲突
# 匿名函数也是函数对象，也将匿名函数赋值给变量

def build(x, y):
    return lambda: x + x * y

def testAnonyFunction():
    mapFuncSample = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7]))
    print(mapFuncSample)

    anonyFuncPtr = lambda x: x * x
    print(anonyFuncPtr)
    print(anonyFuncPtr(3))

    # 匿名函数也可以作为返回值
    print(build(3, 4))
    buildPtr = build(3, 4)
    print(buildPtr())
