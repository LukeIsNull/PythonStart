#!/usr/bin/env python3
#coding:utf-8

import psutil

def testPsutil():
    print(psutil.cpu_count()) # CPU逻辑数量
    print(psutil.cpu_count(logical=False)) # CPU物理核心

    print(psutil.cpu_times()) # 统计CPU的用户／系统／空闲时间

    print(psutil.virtual_memory()) # 获取内存信息

    print(psutil.swap_memory()) # 交换内存信息

    print(psutil.disk_partitions()) # 磁盘分区信息

    print(psutil.disk_usage('/')) # 磁盘使用情况

    print(psutil.net_io_counters()) # 获取网络读写字节／包的个数)

    print(psutil.net_if_addrs()) # 获取网络接口信息

    print(psutil.net_if_stats()) # 获取网络接口状态
