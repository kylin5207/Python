# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
多线程共享全局变量2：
   当多个线程共享全局变量时，会出现安全问题
   没有控制多个线程对同⼀资源的访问，对数据造成破坏，使得线程运⾏的结果不可预期
"""
import threading
import time

# 定义一个全局变量
num = 0


def modify1(temp):
    global num
    for i in range(temp):
        num += 1

    print("----in modify1 num = %d --------" % num)


def modify2(temp):
    global num
    for i in range(temp):
        num += 1
    print("----in modify2 num = %d --------" % num)


def main():
    #  参数target指定将来这个线程去哪个函数执行代码
    # args指定将来调用函数的时候，传递什么数据进去
    t1 = threading.Thread(target=modify1, args=(10000000,))
    t2 = threading.Thread(target=modify2, args=(10000000,))

    t1.start()
    t2.start()

    time.sleep(1)

    print("----in main num = %d --------" % num)


if __name__ == "__main__":
    main()
