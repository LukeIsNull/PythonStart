#!/usr/bin/env python3
#coding:utf-8

from types import MethodType

class Student(object):
    pass

def set_age(self, age):
    self.age = age

def set_score(self, score):
    self.score = score

class Student2(object):
    __slots__ = ('name', 'age')
    pass

class Student3(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

class Student4(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

class Student5(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

def testClassProperty():
    s = Student()
    s.name = 'Michael'
    # 给实例绑定一个方法
    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)
    # 给一个实例绑定的方法，对另一个实例是不起作用的
    # 为了给所有实例都绑定方法，可以给class绑定方法
    Student.set_score = set_score
    t = Student()
    s.set_score(99)
    t.set_score(60)
    print(s.score)
    print(t.score)

    # 使用__slots__限制实例的属性
    # 在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    s2 = Student2()
    s2.name = 'Lily'
    s2.age = 8
    #s2.score = 100 # error
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

    s3 = Student3()
    s3.set_score(88)
    print(s3.get_score())
    #s3.set_score(-1) # error

    # Python内置的@property装饰器就是负责把一个方法变成属性调用
    s4 = Student4()
    s4.score = 100
    print(s4.score)
    # s4.score = 999 # error

    # 只定义getter方法，不定义setter方法就是一个只读属性
    # 特别注意：属性的方法名不要和实例变量重名
    s5 = Student5()
    s5.birth = 2000
    print(s5.birth)
    print(s5.age)
    s5.age = 10 # error
