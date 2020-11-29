# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
装饰器实例：
    使用装饰器对有参数的函数进行装饰
"""

from time import ctime, sleep
# ctime()计算调用时间
# 函数.__name__ 获取函数名
# sleep()用于系统休眠一段时间，单位是秒


def timefunc(func):
    def func_in(a, b):
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return func_in


@timefunc
def pricing(a, b):
    print("The price is %d" % (a + b))


if __name__ == "__main__":
    pricing(2, 3)
    sleep(2)
    pricing(6, 6)
