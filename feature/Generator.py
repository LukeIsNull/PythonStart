#!/usr/bin/env python3
#coding:utf-8

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
    # function including 'yield' is a generator function
    # calling generator function will return a generator
        print('Before yield keyword')
        yield b
        print('After yield keyword')
        a, b = b, a + b
        n = n + 1
    return 'done'

def Generator():
    # create a generator
    # Note: it uses () instead of []
    g = (x * x for x in range(10))
    print(g)

    # print element of generator in two ways:
    # 1. use function next()
    print(next(g))
    # 2. use for loop
    for n in g:
        print(n)

    # Fibonacci function realized using generator
    o = fib(5)
    print(o)
    print(next(o))
    # Note: Once calling generator function will
    # create one object. Several-times calling result
    # in several individual objects.
    for n in fib(6):
        print(n)
