# -*- coding:utf-8 -*-
"""
classTest 新式类和经典类的学习

# 新式类的方法解析顺序，采用的式从左到右，广度优先的方式进行查找

:Author: Shangmengqi@tsingj.com
:Last Modified by: Shangmengqi@tsingj.com
"""

# 新式类
class A():
    def name(self):
        return 'A'


class B(A):
    pass


class C(A):
    def name(self):
        return 'C'


class D(B, C):
    pass


if __name__ == "__main__":
    # 测试新式类
    print(D().name())
    print(type(A))
