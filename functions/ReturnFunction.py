#!/usr/bin/env python3
#coding:utf-8

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

def testReturnFunction():
    f1 = lazy_sum(1, 3, 5, 7, 9)
    print(f1)
    print(f1())
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 == f2)
    # 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
    f3, f4, f5 = count()
    print(f3())
    print(f4())
    print(f5())
    # 创建一个函数，用该函数的参数绑定循环变量当前的值
    f3, f4, f5 = count2()
    print(f3())
    print(f4())
    print(f5())
    # 如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错
    # 在fn()函数内部加一个nonlocal x的声明，解释器把fn()的x看作外层函数的局部变量，它已经被初始化
    f6 = inc()
    print(f6())
    # 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量
