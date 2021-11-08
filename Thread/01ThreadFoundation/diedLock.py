# -*- coding:utf-8 -*-
"""
diedLock 死锁演示，无法正常终止

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name + " : up")
            time.sleep(1)

            if mutexB.acquire():
                print(self.name + " : down")
                mutexB.release()
            mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name + " : up")
            time.sleep(1)

            if mutexA.acquire():
                print(self.name + " : down")
                mutexA.release()
            mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == "__main__":
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()