#!/usr/bin/env python3
#coding:utf-8

from io import StringIO
from io import BytesIO

# stringIo就是在内存中读写str
def testStringIo():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())

    f1 = StringIO('Hello!\nHi!\nGoodBye!')
    while True:
        s = f1.readline()
        if s == '':
            break
        print(s.strip())

# bytesIo操作二进制数据
# BytesIO实现了在内存中读写bytes
def testBytesIo():
     f = BytesIO()
     f.write('中文'.encode('utf-8'))
     print(f.getvalue())

     f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
     f1.read()

def testStringIoBytesIo():
    testStringIo()
    testBytesIo()
