#!/usr/bin/env python3
#coding:utf-8

import unittest

class myDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
        
    def __setattr__(self, key, value):
        self[key] = value

class TestDict(unittest.TestCase):
    # setUp&tearDown分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('setUp...')

    def test_init(self):
        d = myDict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = myDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = myDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = myDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = myDict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        print('tearDown...')

if __name__ == '__main__':
    unittest.main()
