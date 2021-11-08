# -*- coding:utf-8 -*-
"""
consumerAndProducer 多线程版本的消费者和生产者

⽣产者消费者模式是通过⼀个容器来解决⽣产者和消费者的强耦合问题。
  ⽣产者和消费者彼此之间不直接通讯，⽽通过阻塞队列来进⾏通讯，所以⽣产者⽣产完数据之后不⽤等待消费者处理，直接扔给阻塞队列，消费者不找⽣
产者要数据，⽽是直接从阻塞队列⾥取，阻塞队列就相当于⼀个缓冲区，平衡了⽣产者和消费者的处理能⼒。

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
import threading
import time
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 100:
                for i in range(10):
                    count = count+1
                    msg = f"{self.name}生成产品{count}"
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = f"{self.name}取出{queue.get()}"
                    print(msg)
            time.sleep(0.5)


if __name__ == '__main__':
    queue = Queue()
    for i in range(200):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()