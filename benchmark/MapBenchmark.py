#!/usr/bin/env python3
#coding:utf-8

from line_profiler import LineProfiler

def doSquare(x):
    return x * x

def mapFunc(func, numbers):
    res = map(func, numbers)
    return res

def loopFunc(func, numbers):
    res = []
    for num in numbers:
        res.append(func(num))

    return res

def mapBenchmark():
    mapBench = LineProfiler()
    mapBench_wrap = mapBench(mapFunc)
    mapBench_wrap = mapBench_wrap(doSquare, range(10))
    mapBench.print_stats()

    loopBench = LineProfiler()
    loopBench_wrap = loopBench(loopFunc)
    loopBench_wrap = loopBench_wrap(doSquare, range(10))
    loopBench.print_stats()
