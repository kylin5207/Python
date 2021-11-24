# -*- coding:utf-8 -*-
"""
attribute

_get_ 和 _getattr_ 和 _getattribute_ 的区别于联系
get，getattr, getattribute 都是访问属性的方法，但是不太相同
· “object.__getattribute__(self, name)”
无条件的被调用，通过实例访问实例。如果class中定义了 getattr() ，则getattr() 不会被调用，除非显示调用或引发attributeERROR异常

·  object.__getattr__(self, name)
当一般位置找不到属性时，会调用getattr，返回一个值或 AttributeError 异常

·  object.__get__(self, instance, owner)
如果class定义了它，则这个class就可以称为descriptor。owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。（descriptor的实例自己访问自己是不会触发get，而会触发call，只有descriptor作为其它类的属性才有意义。）

由上述例子看出：
1. 每次通过实例访问属性，都会触发getattribute方法。
2. 当通过实例访问的属性不存在时，仍然触发 getattribute，不过接着要触发 getattr，这是个异常处理
3. 每次访问 描述符（即实现了get的类），都会先经过 get方法。
4. 需要注意的是，当使用类访问不存在的变量时，不会触发 getattr 方法。而描述符不存在此问题，只是把实例 标识为None 而已。

:Author: Shangmengqi@tsingj.com
:Last Modified by: Shangmengqi@tsingj.com
"""
class A:
    att = "abc"
    def __getattribute__(self, item):
        print("触发__getattribute__()")
        return object.__getattribute__(self, item) + ' from getattribute'

    def __getattr__(self, item):
        print("触发__getattr__()")
        return item + 'from getattr'

    def __get__(self, instance, owner):
        print("触发__get__()方法", instance, owner)
        return self

class B:
    a1 = A()

if __name__ == "__main__":
    a2 = A()
    b = B()
    print("-"*30)
    print(a2.att)

    print("-"*30)
    print(a2.kylin)

    print("-"*30)
    print(b.a1)

    print("-"*30)
    print(b.a1.att)

    print("-"*30)
    print(b.a1.att2)

