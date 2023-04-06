#!/usr/bin/env python3
#coding:utf-8

from datetime import datetime, timedelta

# 注意到datetime是模块，datetime模块还包含一个datetime类
# 通过from datetime import datetime导入的才是datetime这个类
# 如果仅导入import datetime，则必须引用全名datetime.datetime

def testDateTime():
    now = datetime.now()
    print(now)

    # 指定某个日期和时间
    dt = datetime(2022, 4, 1, 15, 30)
    print(dt)

    # timestamp
    # epoch time: 1970-1-1 00:00:00
    print(dt.timestamp())

    t = 60.0
    # UTC+8:00
    print(datetime.fromtimestamp(t))
    # UTC+0:00
    print(datetime.utcfromtimestamp(t))

    # from str to datetime
    # 注意转换后的datetime是没有时区信息的
    cday = datetime.strptime('2022-04-01 15:30:00', '%Y-%m-%d %H:%M:%S')
    print(cday)
    print(type(cday))

    sday = cday.strftime('%a, %b %d %H:%M')
    print(sday)
    print(type(sday))

    dayOffset = timedelta(hours = 1)
    print((now + dayOffset))
    print((now - dayOffset))

    # 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
