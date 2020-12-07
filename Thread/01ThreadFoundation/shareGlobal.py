# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
多线程共享全局变量
"""
import threading
import time

# 定义一个全局变量
num = 100
nums = [11, 22]


def modify1(temp):
    global num
    num += 1
    temp.append(33)

    print("----in modify1 num = %d --------" % num)
    print("----in modify1 nums = %s --------" % str(temp))


def modify2():
    print("----in modify2 num = %d --------" % num)
    print("----in modify2 nums = %s --------" % str(nums))


def main():
    #  参数target指定将来这个线程去哪个函数执行代码
    # args指定将来调用函数的时候，传递什么数据进去
    t1 = threading.Thread(target=modify1, args=(nums,))
    t2 = threading.Thread(target=modify2)
    t1.start()

    time.sleep(1)

    t2.start()

    time.sleep(1)

    print("----in main num = %d --------" % num)


if __name__ == "__main__":
    main()
