#!/usr/bin/env python3
#coding:utf-8

import logging

def myDivide(diviend):
    try:
        print('try...')
        r = 10 / int(diviend)
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    except ValueError as e:
        print('ValueError:', e)
    # Python的错误其实也是class，所有的错误类型都继承自BaseException
    # 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
    except UnicodeError as e:
        print('UnicodeError:', e) # 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

def bar(s):
    return foo(s) * 2

def callBarFoo():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

def testErrorHandling():
    myDivide(0)
    myDivide('a')

    callBarFoo()

    print('End')
