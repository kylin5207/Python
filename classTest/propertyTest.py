# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
property属性
    1。 便捷化对私有属性进行getter和setter操作
    2。 把方法进行封装，开发者操作更方便
可以使用装饰器
"""


class Method(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num

    # 在这时候，根据实际场景判断是调用setter还是getter方法
    num = property(getNum, setNum)


class Method2(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, newNum):
        if isinstance(newNum, int):
            self.__num = newNum
        else:
            print("不是整型数据")


if __name__ == "__main__":
    print("=====传统方法=====")
    method = Method()
    method.num = 200
    print(method.getNum())
    print(method._Method__num)
    print("-" * 20)

    print("=====使用装饰器=====")
    method2 = Method2()
    method2.num = 200
    print(method2._Method2__num)


