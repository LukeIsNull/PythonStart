#!/usr/bin/env python3
#coding:utf-8

# Two inputs for filter():
# 1. function 2. sequence
# Filter implements every elements using function
# and select results according to return value.
# The return of filter is Iterator

def is_odd(n):
    return n % 2 == 1

def not_empty(s):
    return s and s.strip()

def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)

def testFilter():
    resOdd = list(filter(is_odd, range(20)))
    print(resOdd)

    resEmpty = list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
    for word in ['A', '', 'B', None, 'C', ' ']:
        if not_empty(word):
            print('True')
        else:
            print('False')
    print(resEmpty)

    for n in primes():
        if n < 20:
            print(n)
        else:
            break

