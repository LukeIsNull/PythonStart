#!/usr/bin/env python3
#coding:utf-8

import types

def fn():
    pass

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

def testGetObjInfo():
    print(type(fn) == types.FunctionType)
    print(type(lambda x: x) == types.LambdaType)

    # 能用type()判断的基本类型也可以用isinstance()判断
    isinstance('a', str)
    isinstance([1, 2, 3], (list, tuple))

    # 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
    print(dir('ABC'))
    print(len('ABC'))
    print('ABC'.__len__())

    # 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
    obj = MyObject()
    print(hasattr(obj, 'x'))
    print(obj.x)
    print(hasattr(obj, 'y'))
    setattr(obj, 'y', 19)
    print(hasattr(obj, 'y'))
    print(getattr(obj, 'y'))
    # print(getatter(obj, 'z')) # 试图获取不存在的属性，会抛出AttributeError的错误
    print(getattr(obj, 'z', 404)) # 可以传入一个default参数，如果属性不存在，就返回默认值
    # 也可以获得对象的方法
    print(hasattr(obj, 'power'))
    print(getattr(obj, 'power'))
    func = getattr(obj, 'power')
    print(func)
    func()
