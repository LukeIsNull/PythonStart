#!/usr/bin/env python3
#coding:utf-8

from collections import namedtuple, deque, OrderedDict

def testNamedTuple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)

    print(isinstance(p, Point))
    print(isinstance(p, tuple))

    # deque是为了高效实现插入和删除操作的双向列表
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)

    # 使用dict时，Key是无序的
    # 如果要保持Key的顺序，可以用OrderedDict
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print(d)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)

    # 注意，OrderedDict的Key会按照插入的顺序排列
    od['z'] = 1
    od['y'] = 2
    print(od)
