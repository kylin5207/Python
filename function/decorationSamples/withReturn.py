# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
装饰器实例：
    使用装饰器对带返回值的函数进行装饰
"""

from time import ctime, sleep
# ctime()计算调用时间
# 函数.__name__ 获取函数名
# sleep()用于系统休眠一段时间，单位是秒


def timefunc(func):
    def func_in(*args, **kwargs):
        print("%s called at %s" % (func.__name__, ctime()))
        # 如果func函数中有返回值的话，在内部嵌套的函数中也应该有返回值
        return func(*args, **kwargs)
    return func_in


@timefunc
def pricing(a, b):
    return a + b


@timefunc
def pricing2(a, b, c):
    return a + b + c


if __name__ == "__main__":
    value = pricing(2, 3)
    print(value)