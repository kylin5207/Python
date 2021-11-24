# -*- coding:utf-8 -*-
"""
classTest2 类属性vs实例属性
1. 类属性：定义在类里面但在函数外面的变量，它们都是静态的
2. 实例属性：定义在__init__()方法里的变量，这些属性只有被创建时才会被创建

3. 每次通过实例访问属性，都会经过__getattribute__函数。而当属性不存在时，仍然需要访问__getattribute__，不过接着要访问__getattr__。这就好像是一个异常处理函数。
每次访问descriptor（即实现了__get__的类），都会先经过__get__函数。
:Author: Shangmengqi@tsingj.com
:Last Modified by: Shangmengqi@tsingj.com
"""

class Test:
    # 类属性
    name = "class_attribute"

    def __init__(self):
        # 实例属性
        self.name = "instance_attribute"
        self.age = 18
        # 私有属性
        self.__salary = 2000

    def print(self):
        print(f"name = {self.name}\n"
              f"age = {self.age}\n"
              f"salary = {self.__salary}")

t = Test()
print(Test.name)
print(t.name)
print(Test.name)

# 使用dir可以查看对象的属性
print(dir(Test))
print(dir(t))
print(Test.__dict__)
print(t.__dict__)

t.print()

# 但是，私有化并不是语法上的强制，而是 python 隐藏了私有字段的访问入口，所以我们可以在新的入口中访问到私有字段
# 通过：对象._类__字段名，可以使用类的私有字段
print(t._Test__salary)
