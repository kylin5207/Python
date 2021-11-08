# -*- coding:utf-8 -*-
"""
obj_iterator
实现自定义类的迭代
1. 如果不实现__iter__方法，直接对自定义对象进行迭代，会报TypeError，object is not iterable

2. __iter__()方法返回一个特殊的迭代器对象，这个迭代器对象实现了__next__()方法并通过 StopIteration 异常标识迭代的完成。
3. __next__() 方法会返回下一个迭代器对象。

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
from collections import Iterable


class Student(object):
    """
    想要一个对象成为一个可迭代对象，即可以使用for，那么必须实现__iter__方法和__next__方法
    """
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def main():
    student = Student()
    student.add("Alice")
    student.add("Bob")
    student.add("Candy")

    print("判断student对象是否是可迭代对象：", isinstance(student, Iterable))

    for name in student:
        print(name)


if __name__ == "__main__":
    main()
