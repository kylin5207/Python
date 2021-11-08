# -*- coding:utf-8 -*-
"""
createProcess2 自定义进程类

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
from time import sleep
from multiprocessing import Process


class Run(Process):
    def run(self):
        while True:
            print("Process is running")
            sleep(1)


def main():
    p = Run()
    p.start()


if __name__ == "__main__":
    main()
    print("----Main Thread finished--------")

