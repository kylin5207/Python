# -*- coding:utf-8 -*-
"""
mutexLock 互斥锁——解决死锁局面的一种方式

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
from threading import Thread, Lock
from time import sleep


class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("------Task 1 -----")
                sleep(0.5)
                lock2.release()


class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("------Task 2 -----")
                sleep(0.5)
                lock1.release()

lock1 = Lock()
lock2 = Lock()


def main():
    t1 = Task1()
    t2 = Task2()
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()