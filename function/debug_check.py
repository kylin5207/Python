"""
调试定位方法
"""
import inspect


def __line__():
    return inspect.currentframe().f_back.f_lineno

class Person:
    def __init__(self, age):
        self.age = age
        self.count = 0

    def add_data(self, num):
        self.count += num
        print(f"I'm {__file__} on line {__line__()}!")

person = Person(20)
person.add_data(2)

