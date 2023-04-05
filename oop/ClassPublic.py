#!/usr/bin/env python3
#coding:utf-8

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private)
# 只有内部可以访问，外部不能访问

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'

    def print_grade(self):
        print('%s: %s' % (self.__name, self.__get_grade()))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

def testClassPublic():
    bart = Student('Bart Simpson', 95)
    bart.print_grade()
    bart.__name = 'Alex Simpson'
    bart.print_grade()
    print(bart.__name)
    # 不能直接访问__name是因为
    # Python解释器对外把__name变量改成了_Student__name
    print(bart._Student__name)

    # 通过bart.__name = 'Alex Simpson'设置私有变量是错误的
    # 虽然设置“成功”，但是这个__name和内部的__name并不是一个变量
    # 内部的__name已经被python解释器自动改成了_Student__name
    # 通过这种方法设置，实际是给bart新增了一个__name外部变量

    print(bart.get_name())
    print(bart.get_score())

    print(bart.__get_grade()) # error: private function
