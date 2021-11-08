# -*- coding:utf-8 -*-
"""
DaemonThread 守护线程
程序运行的时候在后台提供一种通用服务的线程
程序中主线程及所有非守护线程执行结束时，未执行完毕的守护线程也会随之消亡，程序将结束运行。

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
from time import sleep
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = count

    def run(self):
        for i in range(self.count):
            print(f"{self.name} : {i}")
            sleep(1)


if __name__ == "__main__":
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 5)
    thread2 = myThread(2, "Thread-2", 5)

    # 设置子线程为主线程的守护线程，主线程执行结束，守护线程也结束
    thread1.setDaemon(True)
    thread2.setDaemon(True)

    # 开启新线程
    thread1.start()
    thread2.start()


    print("------Main End-----")


