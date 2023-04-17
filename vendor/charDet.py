#!/usr/bin/env python3
#coding:utf-8

import chardet

# 对于未知编码的bytes，要把它转换成str，需要先“猜测”编码
# 猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”

def testChardet():
    print(chardet.detect(b'Hello, world!'))

    chinese = '床前明月光，疑似地上霜'.encode('gbk')
    print(chardet.detect(chinese))

    japanese = '家に椅子が一つありまし'.encode('utf-8')
    print(chardet.detect(japanese))
