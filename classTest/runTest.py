# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
运行过程中给类添加方法
对象名.方法名 = types.MethodType(方法名，对象名)
"""

import types


class Animal(object):
    def __init__(self, name):
        self.name = name

    def drink(self):
        print("%s drink water~" % self.name)

    def __str__(self):
        print("Animal type: %s" % self.name)


# 这里一定注意，要添加self
def run(self, name):
    print("%s run~" % name)


def main():
    dog = Animal("Dog")
    dog.drink()
    dog.run = types.MethodType(run, dog)
    dog.run(dog.name)


if __name__ == "__main__":
    main()