#!/usr/bin/env python3
#coding:utf-8

def ListGenerator():
    # List generator
    print([x * x for x in range(10)])

    # if...  work as filter
    # Bad demo: print([x * x for x in range(10) if x % 2 == 0 else -x])
    print([x * x for x in range(10) if x % 2 == 0])

    # if... else... work as expression
    print([x * x if x % 2 == 0 else -x for x in range(10)])
