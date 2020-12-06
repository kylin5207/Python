# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import threading
import time

"""
为了让每个线程的封装性更完美，通过继承threading.Thread的方式，定义线程类并重写其中的run方法
这里和java对线程的操作差不多，基本一样
"""


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)  # name属性保存的是当前线程的名字
            print(msg)


if __name__ == "__main__":
    t = MyThread()
    t.start()

