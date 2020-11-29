# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
装饰器实例：
    使用装饰器对无参数的函数进行装饰
"""


def func(functionName):
    """
    里面除了内部对函数不会执行，其他语句都会执行
    :param functionName:
    :return:
    """
    print("----decorator----")
    print("----1----")

    def func_in():
        print("-----func_in start-------")
        functionName()
        print("-----func_in end------")

    print("----2-----")
    print("----3----")
    return func_in

@func
def pricing():
    print("---pricing---")


if __name__ == "__main__":
    pricing()