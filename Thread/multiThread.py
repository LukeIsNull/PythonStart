#!/usr/bin/env python3
#coding:utf-8

import time, threading

# Python的标准库提供了两个模块：_thread和threading
# _thread是低级模块，threading是高级模块，对_thread进行了封装。

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)

    print('thread %s ended.' % threading.current_thread().name)

# 多线程和多进程最大的不同在于
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
# 多线程中，所有变量都由所有线程共享
# 所以，任何一个变量都可以被任何一个线程修改

def testMultiThread():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target = loop, name = 'LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
