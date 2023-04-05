#!/usr/bin/env python3
#coding:utf-8

class Student(object):
    def __init__(self, name):
        self.name = name

class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student2 object (name: %s)' % self.name

class Student3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student2 object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        
class Student4(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student2 object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    
    def __call__(self):
        print('My name is %s.' % self.name)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
        
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

def testCustomizedClass():
    print(Student('Mike'))

    print(Student2('Mary'))

    s2 = Student2('Mary')
    print(s2)

    s3 = Student3('Lily')
    print(s3)

    for n in Fib():
        print(n)

    print(Fib()[5])
    print(Fib()[0:5])

    # print(s2.score) # error
    print(s3.score)
    print(s3.abc)

    s4 = Student4('Andy')
    #print(s4.abc) # error
    print(s4())
    # 判断一个变量是函数还是对象
    print(callable(s4()))
    print(callable(Student('aaa')))
    print(callable('abc'))

    # 利用完全动态的__getattr__，实现一个链式调用
    print(Chain().status.user.timeline.list)
