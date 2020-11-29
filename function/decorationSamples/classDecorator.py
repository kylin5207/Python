# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
装饰器实例：类装饰器
    装饰器函数其实是这样⼀个接⼝约束，它必须接受⼀个callable对象作为参数， 然后返回⼀个callable对象。
    在Python中⼀般callable对象都是函数，但也有例外。
    只要某个对象重写了 __call__() ⽅法， 那么这个对象就是callable的。
"""


class W(object):
    def __init__(self, func):
        print("===初始化====")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self):
        print("类装饰器")
        self.__func()


@W
def calculate():
    print("calculate")


if __name__ == "__main__":
    calculate()




