#!/usr/bin/env python3
#coding:utf-8

from functools import reduce

def demoMapFunc(x):
    return x * x

def demoReduceFunc(x, y):
    return x + y

def demoMapAndReduceFunc(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

def MapAndReduce():
    print('Demo for MapAndReduce function:')
    output = reduce(demoMapAndReduceFunc, map(char2num, '13579'))
    print(output)
    print('Demo for MapAndReduce function with lambda:')
    output = reduce(lambda x, y: x * 10 + y, map(char2num, '13579'))
    print(output)

def Reduce():
    # reduce(f, [x1, x2, x3, x4])
    # -> f(f(f(x1, x2), x3), x4)
    print('Demo for reduce function:')
    output = reduce(demoReduceFunc, [x for x in range(10) if x % 2 == 1])
    print(output)

def Map():
    # Two inputs for map function:
    # 1. function; 2. Iterable
    # map function do mapping from input
    # iterable to output using input function
    print('Demo for map function:')
    output = map(demoMapFunc, range(10))
    print(list(output))

# Test_1:
def normalize(s):
    return s[0].upper() + s[1:].lower()

def TestMap():
    input = ['adam', 'LISA', 'barT']
    output = map(normalize, input)
    print(list(output))

# Test_2:
def prod(L1, L2):
    return L1 * L2

def TestReduce():
    input = [1, 3, 5, 7, 9]
    output = reduce(prod, input)
    print(output)

# Test_3:
def str2floatEntry(s):
    output = reduce(lambda x, y: 10 * x + y, map(char2num, s))
    return output

def TestMapAndReduce():
    input = '123.456'
    output = map(str2floatEntry, input.split('.'))
    print(output[0] + output[1])
