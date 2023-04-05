#!/usr/bin/env python3
#coding:utf-8

import os
import subprocess
import time
import random

from multiprocessing import Process, Queue

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
# 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次。
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。
# 子进程需要调用getppid()就可以拿到父进程的ID。

def printCurrentPid():
    print('Process (%s) start...' % os.getpid())

def createChildProcess():
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

def testSubProcess():
    print('$ nslookup www.python.org')

    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s ' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

def processCommun():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

def testMultiProcess():
    printCurrentPid()

    createChildProcess()

    testSubProcess()

    processCommun()
