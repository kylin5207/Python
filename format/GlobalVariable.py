# -*- coding:utf-8 -*-
"""
GlobalVariable 线程共享全局变量

1. 什么时候给变量加上global声明？
在一个函数中对全局变量进行修改的时候，是否需要global对变量进行说明需要看该变量是否是可变对象。
对于不可变对象，修改该变量，改变其指向，让全局变量指向一个新的空间，需要使用global声明。
对于可变对象，只是修改了变量的内容，其指向没有改变，所以不用加global。

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""

num = 10
nums = [1, 2]

def test1():
    global num
    num +=10

def test2():
    nums.append(3)

test1()
test2()
print(num)
print(nums)

