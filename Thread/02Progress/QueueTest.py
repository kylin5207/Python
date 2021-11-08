# -*- coding:utf-8 -*-
"""
QueueTest 消息队列实现多进程的数据通信

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""

from time import sleep
from multiprocessing import Queue

# 初始化一个Queue对象，最多可接受三条put信息
q = Queue(3)

# 使用put()方法将数据存放到Queue对象中
# 如果Queue存满，再放入数据会阻塞
q.put("消息1")
q.put(2)
q.put([1.2, 3.2])

# full()和empty()方法查看消息队列的存储情况
print(q.full())
print(q.empty())

# 使用get()方法将数据从Queue中取出数据,获取队列中的⼀条消息，然后将其从列队中移除
# 如果queue中没有数据，则会等待
print(q.get())
print(q.get())
print(q.get())

# # put_nowait()和get_nowait()无需阻塞，直接用异常的形式告诉结果
#
# 推荐的安全模式
# 写入时，先判断消息队列是否存满
if not q.full():
    q.put_nowait("新消息")
    sleep(1)

# 读取时，先判断消息队列是否非空
if not q.empty():
    print(q.get_nowait())

