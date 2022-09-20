"""
方法参数的定义
- 首先对于直接赋值的参数，方法默认按顺序占位

- 可变参数(*args)，args接受元组对象
- 可变关键字参数(**kwargs)， args接受字典对象

"""

def method(*args):
    for arg in args:
        print(arg)

def method2(**args):
    for arg in args:
        print(arg)

# method(name="kylin", score=88)
# TypeError: method() got an unexpected keyword argument 'name'

method(2,3)
method2(name="kylin", score=88)