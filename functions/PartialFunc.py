#!/usr/bin/env python3
#coding:utf-8

# functools.partial的作用:
# 把一个函数的某些参数给固定住（也就是设置默认值）
# 返回一个新的函数，调用这个新函数会更简单

import functools

def testPartialFunc():
    int2 = functools.partial(int, base=2)
    print(int2('1011'))
    print(int2('1000000', base=10))
