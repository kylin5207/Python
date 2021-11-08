# -*- coding:utf-8 -*-
"""
processPool 进城池
1. 在利用python实现并行时：
  并发执行的任务通常远大于核数
  一个操作系统不可能无限开启进程
  进程开启过多，效率反而下降（开启进程需要占用系统资源）
2. 当被操作对象数目不大时，可以直接利用multiprocessing.Process手动生成进程
3. 通过维护一个进程池来控制进程数目，节省了进城创建和销毁的时间
(1)初始化Pool时，可以指定一个最大进程数
(2)当有新的请求提交到Pool中时， 如果池还没有满，那么就会创建⼀个新的进程来执行该请求
(3)池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行


:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
from multiprocessing import Pool
import os, time
from time import sleep


def worker(msg):
    t_start = time.time()
    print(f"{msg}开始执行, 进程号为{os.getpid()}")

    sleep(2)
    t_stop = time.time()
    print(f"{msg}执行完毕，耗时{t_stop - t_start}")


def main():
    pool = Pool(3)

    print("------start-------")

    for i in range(10):
        pool.apply_async(worker, (i,))

    # map()函数会将第二个参数的需要迭代的列表元素一个个的传入第一个参数我们的函数中，第一个参数是我们需要引用的函数，这里我们看到第一个参数我们自己定义的函数并没有设置形参传值。
    # pool.map(worker, list(range(10)))
    pool.close()  # 关闭进城池，关闭后pool不再接受新的请求
    pool.join()  # 主进程阻塞，等待pool中所有子进程执行完成，必须放在close语句之后
    print("-----end------")


if __name__ == "__main__":
    main()