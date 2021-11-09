# -*- coding:utf-8 -*-
"""
fibnacci 用迭代器实现斐波那契数列
迭代器最核心的功能就是可以通过__next__方法的调用来返回下一个值。
而这个值不是从已有的数据中读取的，而是通过程序按照一定的规则生成的。
这也就意味着我们可以不再依赖一个现存的数据集合来存放数据，而是边用边生成，这样的好处就是可以节省大量的内存空间。


:Author: Shangmengqi@tsingj.com
:Last Modified by: Shangmengqi@tsingj.com
"""

import time

class Fibnacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        """
        iter方法返回一个特殊的迭代器对象
        :return:
        """
        return self

    def __next__(self):
        """
        StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
        """
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def main():
    fibo = Fibnacci(10)

    # 使用迭代器的方式一：for循环遍历
    # for num in fibo:
    #     print(num)
    #     time.sleep(1)

    # 使用迭代器的方式二：可以用list,tuple接受迭代器，转换成一个可迭代对象
    fibo_list = list(fibo)
    print(fibo_list)


if __name__ == "__main__":
    main()
