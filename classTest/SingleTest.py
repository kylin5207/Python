# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
单例对象测试
单例：系统中只有唯一的一个实例
1. 重写__new__()方法
2. 调用父类方法分配空间，并返回对象的引用
"""


class Single(object):

    # 记录被创建对象的引用
    instance = None

    def __new__(cls):

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def do(self):
        print("工作")


a = Single()
b = Single()
print("%x" % id(a))
print("%x" % id(b))
print(a is b)