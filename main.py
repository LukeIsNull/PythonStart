#!/usr/bin/env python3
#coding:utf-8

import sys

from pathlib import Path

# From feature folder
from feature.ListGenerator import ListGenerator
from feature.Generator import Generator
from feature.Iterator import Iterator
# From functions folder
from functions.MapReduce import Map, Reduce, MapAndReduce, TestMapAndReduce
from functions.Filter import testFilter
from functions.Sorted import testSorted
from functions.ReturnFunction import testReturnFunction
from functions.AnonyFunction import testAnonyFunction
from functions.Decorator import testDecorator
from functions.PartialFunc import testPartialFunc
# From module folder
from module import Module
# From oop folader
from oop.Class import testClass
from oop.ClassPublic import testClassPublic
from oop.SubClass import testSubClass
from oop.GetObjInfo import testGetObjInfo
from oop.ClassInfo import testClassInfo
# From oopPlus folder
from oopPlus.ClassProperty import testClassProperty
from oopPlus.CustomizedClass import testCustomizedClass
from oopPlus.EnumClass import testEnumClass
from oopPlus.MetaClass import testMetaClass
# From debug folder
from debug.ErrorHandling import testErrorHandling
from debug.Debugging import testDebug
# From fileIO folder
from fileIO.fileWR import testFileWR
from fileIO.stringIoBytesIo import testStringIoBytesIo
from fileIO.fileAndDir import testFileAndDir
from fileIO.serialize import testSerialize
# From Thread folder
from Thread.multiProcess import testMultiProcess
from Thread.multiThread import testMultiThread
from Thread.threadLocal import testThreadLocal
# From toolModule folder
from toolModule.dateTime import testDateTime
from toolModule.namedTuple import testNamedTuple

def main():
    # ListGenerator()
    # Generator()
    # Iterator()

    # Map()
    # Reduce()
    # MapAndReduce()
    # TestMapAndReduce()
    # testFilter()
    # testSorted()
    # testReturnFunction()
    # testAnonyFunction()
    # testDecorator()
    # testPartialFunc()

    # Module.test()

    # testClass()
    # testClassPublic()
    # testSubClass()
    # testGetObjInfo()
    # testClassInfo()

    # testClassProperty()
    # testCustomizedClass()
    # testEnumClass()
    # testMetaClass()

    # testErrorHandling()
    # testDebug()

    # testFileWR()
    # testStringIoBytesIo()
    # testFileAndDir()
    # testSerialize()

    # testMultiProcess()
    # testMultiThread()
    # testThreadLocal()

    # testDateTime()
    testNamedTuple()

if __name__ == '__main__':
    main()
