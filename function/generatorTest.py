# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
生成器Generator
有点像java中的iterator迭代器
  1. ⽣成器是这样⼀个函数，它记住上⼀次返回时在函数体中的位置。对⽣成器函数的第⼆次（或第n次）调⽤跳转⾄该函数中间， ⽽上次调⽤的所有局部变量都保持不变
  2. ⽣成器不仅“记住”了它数据状态； ⽣成器还“记住”了它在流控制构造（在命令式编程中，这种构造不只是数据值）中的位置
优点：
    节约内存
    
"""
from collections.abc import Iterator

def fib(times):
    n = 0
    a, b = 0, 1

    while n < times:
        yield b
        a, b = b, a+b
        n += 1
    return


def test1():
    G = (x*2 for x in range(5))

    # 1. 通过next方法获得生成器的下一个返回值
    # 不推荐，最好用for
    print(next(G))
    print(next(G))
    print(next(G))
    print(next(G))


def test2(num):
    # 使用for循环便利
    for n in fib(num):
        print(n)


# 2. 使用yield
if __name__ == "__main__":
    # test1()
    test2(5)
    
    # 如何判断是否可迭代
    print("Is it iteratable? {}".format(isinstance(fib(4), Iterator)))


