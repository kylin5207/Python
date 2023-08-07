"""
如何我们在创建类后将函数注册为类中的方法？
允许我们将一个类的实现拆分为多个代码块。
"""

# 注解函数
def add_to_class(Class):  #@save
    """Register functions as methods in created class."""
    def wrapper(obj):
        setattr(Class, obj.__name__, obj)
    return wrapper


# 我们可以先声明类a并创建一个实例a
class A:
    def __init__(self):
        self.b = 1

@add_to_class(A)
def do(self):
    print('Class A attribute "b" is', self.b)


a = A()
a.do()
