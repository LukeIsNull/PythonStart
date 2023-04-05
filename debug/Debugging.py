#!/usr/bin/env python3
#coding:utf-8

import logging
import pdb
logging.basicConfig(level = logging.INFO)

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def foo2(s):
    n = int(s)
    pdb.set_trace()
    logging.info('n = %d' % n)
    return 10 / n

def testDebug():
    # 断言
    # Python解释器时可以用-O参数来关闭assert
    # foo('0')

    # logging
    foo2('0')
