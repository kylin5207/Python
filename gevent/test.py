# -*- coding:utf-8 -*-
"""
test gevent协程
在I/O时间自动进行协程的切换
注意：需要将所有的延时阻塞操作，全都替换为gevent.sleep

:Author: Shangmengqi@tsingj.com
:Last Modified by: Shangmengqi@tsingj.com
"""
import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


print("-----1---")
g1 = gevent.spawn(f, 5)
print("-----2---")
g2 = gevent.spawn(f, 5)
print("-----3---")
g3 = gevent.spawn(f, 5)
print("-----4---")

g1.join()
g2.join()
g3.join()