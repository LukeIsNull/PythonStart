#!/usr/bin/env python3
#coding:utf-8

import threading

local_school = threading.local()

# 在多线程环境下，每个线程都有自己的数据。
# 一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程
# 而全局变量的修改必须加锁，但是局部变量在函数调用的时候，传递起来很麻烦

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

def testThreadLocal():
    t1 = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
    t2 = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
