# -*- coding:utf-8 -*-
"""
JoinThread 控制线程执行的顺序
join()在程序指定位置，优先让该方法的调用者使用 CPU 资源。
这将阻止调用线程，直到调用其join()方法的线程终止——正常终止或通过未处理的异常终止，或者直到出现可选超时。

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

    thread1.join()
    thread2.join()

    print("------Main End-----")


