# -*- coding:utf-8 -*-
"""
ipcInPool 进程池中的进程通信

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
from multiprocessing import Manager, Pool
import os


def reader(q):
    print(f"reader启动({os.getpid()}), 父进程为({os.getppid()})")
    for i in range(q.qsize()):
        print(f"reader从Queue获得消息：{q.get(True)}")


def writer(q):
    print(f"writer启动({os.getpid()}), 父进程为({os.getppid()})")
    for i in range(10):
        q.put(i)


def main():
    print(f"-----{os.getpid()} start-----")
    q = Manager().Queue()
    pool = Pool(3)

    # 使用阻塞模式创建进程
    pool.apply(writer, (q,))
    pool.apply(reader, (q,))
    pool.close()
    pool.join()

    print(f"-----{os.getpid()} end-----")


if __name__ == "__main__":
    main()
