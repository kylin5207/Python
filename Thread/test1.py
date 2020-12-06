# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import threading
import time

"""
线程测试1：
    系统中最少有一个Main线程在运行，可以用len(threading.enumerate())查看当前线程个数
    当调用threading.Thread的时候，并不会创建线程，在调用start()时才会创建线程以及让其运行
"""


def greet():
    """
    子线程
    :return:
    """
    for i in range(5):
        print("Hello～")
        time.sleep(1)


def bye():
    """
    子线程
    :return:
    """
    for i in range(5):
        print("Bye～")
        time.sleep(1)


if __name__ == "__main__":  # 主线程

    t1 = threading.Thread(target=greet)  # 创建线程
    t2 = threading.Thread(target=bye)  # 创建线程

    print("当前线程信息 %s" % str(threading.enumerate()))

    t1.start()  # 启动线程1

    time.sleep(1)
    print("-" * 20)

    t2.start()  # 启动线程2

    # 使用threading.enumerate()可以获取列表
    print(threading.enumerate())

    while True:
        # 使用len(threading.enumerate())获取当前运行线程个数
        thread_nums = len(threading.enumerate())
        print("当前线程个数：%d" % thread_nums)

        if thread_nums <= 1:
            print("执行完毕")
            break

        time.sleep(0.5)






