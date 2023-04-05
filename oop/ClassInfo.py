#!/usr/bin/env python3
#coding:utf-8

class Student(object):
    name = 'Student'

def testClassInfo():
    s = Student()
    print(s.name)
    print(Student.name)

    s.name = 'Micheal'
    print(s.name)
    print(Student.name)

    del s.name
    print(s.name)
    print(Student.name)
