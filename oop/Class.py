#!/usr/bin/env python3
#coding:utf-8

class Student(object):
    pass

class Student_1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

def testClass():
    bart = Student()
    print(bart)
    print(Student)

    bart.name = 'Bart Simpson'
    print(bart.name)

    bart_1 = Student_1('Bart Simpson', 95)
    print(bart_1.name)
    print(bart_1.score)
    bart_1.print_score()

    lisa = Student_1('Lisa', 99)
    bart_2 = Student_1('Bart', 59)
    print(lisa.name, lisa.get_grade())
    print(bart_2.name, bart_2.get_grade())

    # 和静态语言不同，Python允许对实例变量绑定任何数据
    # 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
    bart_2.age = 8
    print(bart_2.age)
    print(lisa.age) # error
