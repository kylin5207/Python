# -*- coding:utf-8 -*-
"""
compete 资源竞争问题

理想情况：
两个线程都要对全局变量进行加1的操作，各对g_num加n次，g_num的最终结果应该是2n

现实情况：
n小的时候不会出现问题
n大的时候，结果很意外
由于多线程同时操作，可能出现下面的情况：
1. 在g_num = 0时，t1取得g_num = 0。此时，系统将t1调度为sleeping状态，将t2调度为running状态，t2也取得g_num=0
2. t2 实现g_num+=1,此时g_num=1
3. 然后t2调度为sleeping状态，t1调度为running状态。线程t1又把它之前得到的0加1后赋值给g_num
4. 结果就是，t1和t2都实现了g_num+=1，但是的结果g_num = 1


:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
import threading
from time import sleep

g_num = 0

def test1(num):
    global g_num
    for i in range(1, num+1):
        g_num += 1


def test2(num):
    global g_num
    for i in range(1, num+1):
        g_num += 1


def main():
    # 创建线程
    thread1 = threading.Thread(target=test1, args=(10000000,))
    thread2 = threading.Thread(target=test2, args=(10000000,))

    # 开启任务
    thread1.start()
    thread2.start()

    # 设置主线程等待自线程执行完毕
    thread1.join()
    thread2.join()

    print(f"global num = {g_num}")


if __name__ == "__main__":
    main()