# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
多进程的创建和使用

    其实和多线程差不多
"""
import threading
import time
import multiprocessing
import os


def greet():
    """
    子线程
    :return:
    """
    while True:
        print("greet子进程ID %d" % os.getpid())
        print("--------greet------")
        time.sleep(1)


def bye():
    """
    子线程
    :return:
    """
    while True:
        print("bye子进程ID %d" % os.getpid())
        print("--------bye------")
        time.sleep(1)


def main():
    print("主进程ID: %d" % os.getpid())
    p1 = multiprocessing.Process(target=greet)
    p2 = multiprocessing.Process(target=bye)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()