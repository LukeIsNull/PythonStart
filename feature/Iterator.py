#!/usr/bin/env python3
#coding:utf-8

from collections.abc import Iterable, Iterator

def isIterable():
    print('[] is iterable? ' + str(isinstance([], Iterable)))
    print('{} is iterable? ' + str(isinstance({}, Iterable)))
    print('string is iterable? ' + str(isinstance('abc', Iterable)))
    print('integer is iterable? ' + str(isinstance(100, Iterable)))
    print('for loop is iterable? ' + str(isinstance((x for x in range(10)), Iterable)))

def isIterator():
    print('Something goes wrong with error in this function')
    # print('[] is iterator? ' + str(isinstance([], Iterator)))
    # print('{} is iterator? ' + str(isinstance({}, Iterator)))
    # print('string is iterator? ' + str(isinstance('abc', Iterator)))
    # print('integer is iterator? ' + str(isinstance(100, Iterator)))
    # print('for loop is iterator? ' + str(isinstance((x for x in range(10)), Iterator)))

def Iterator():
    # use function isinstance to specify
    # if it it iterable and iterator
    isIterable()
    # Something goes wrong with error
    # 'isinstance() arg 2 must be a type or tuple of types'
    isIterator()
