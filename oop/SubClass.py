#!/usr/bin/env python3
#coding:utf-8

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Dog_1(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    pass

class Cat_1(Animal):
    def run(self):
        print('cat is running...')

    def eat(self):
        print('Eating fish...')

class Timer(object):
    def run(self):
        print('Starting...')

def animal_run(animal):
    animal.run()
    animal.run()

def testSubClass():
    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()

    dog_1 = Dog_1()
    dog_1.run()

    # 判断一个变量是否是某个类型可以用isinstance()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(isinstance(dog, Dog_1))

    # 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
    # 但是，反过来就不行
    animal = Animal()
    print(isinstance(animal, Animal))
    print(isinstance(animal, Dog))

    animal_run(Animal())
    animal_run(Dog_1())

    # 对于静态语言（例如Java）来说，如果需要传入Animal类型
    # 则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
    # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
    # 我们只需要保证传入的对象有一个run()方法就可以
    animal_run(Timer())