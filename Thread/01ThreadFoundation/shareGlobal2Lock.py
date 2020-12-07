# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
使用互斥锁Lock解决资源竞争的问题：
   当多个线程共享全局变量时，会出现安全问题

"""
import threading
import time

# 定义一个全局变量
num = 0


def modify1(temp):
    # 上锁，如果没有被上锁，则上锁成功；
    # 如果上锁前，已经上锁了，则等待锁解除
    # mutex.acquire()

    global num
    for i in range(temp):
        mutex.acquire()
        num += 1
        mutex.release()

    # 解锁
    # mutex.release()

    print("----in modify1 num = %d --------" % num)


def modify2(temp):
    # mutex.acquire()

    global num
    for i in range(temp):
        mutex.acquire()
        num += 1
        mutex.release()

    # mutex.release()

    print("----in modify2 num = %d --------" % num)


# 创建互斥锁，默认没有上锁
mutex = threading.Lock()


def main():
    #  参数target指定将来这个线程去哪个函数执行代码
    # args指定将来调用函数的时候，传递什么数据进去
    t1 = threading.Thread(target=modify1, args=(10000000,))
    t2 = threading.Thread(target=modify2, args=(10000000,))

    t1.start()
    t2.start()

    time.sleep(2)

    print("----in main num = %d --------" % num)


if __name__ == "__main__":
    main()