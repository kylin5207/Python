# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
双装饰器
装饰在调用函数前就已经完成了
"""


def w1(func):
    print("------decorating 1------")

    def inner():
        print("-----正在权限验证1-----")
        func()
    return inner


def w2(func):
    print("------decorating 2------")

    def inner():
        print("-----正在权限验证2-----")
        func()

    return inner


@w1
@w2
def f1():
    print("-----f1------")


if __name__ == "__main__":
    f1()

