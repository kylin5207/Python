# -*- coding:utf-8 -*-
"""
processQueue 使用Queue的多进程通信

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""

from multiprocessing import Queue, Process
from time import sleep
import os


def consumer(q):
    print("Process to consume %s" % os.getpid())
    # 消费者
    while True:
        res = q.get()

        if res is None:
            break

        sleep(2)
        print("%s 吃 %s" % (os.getpid(), res))


def producer(q):
    print("Process to produce %s" % os.getpid())
    # 生产者
    for i in range(1, 10):
        sleep(2)
        res = "包子%s" % i
        q.put(res)
        print("%s 生产 %s" % (os.getpid(), res))
    q.put(None)


def main():
    # 1. 创建队列
    queue = Queue()

    # 2. 创建多个进程，将队列的引用当作实参传递
    p1 = Process(target=producer, args=(queue,))
    c1 = Process(target=consumer, args=(queue,))
    p1.start()
    c1.start()


if __name__ == "__main__":
    main()