# -*- coding:utf-8 -*-
"""
generator 生成器

1. 利用迭代器，可以在每次迭代的时候获取数据，按照特定的规律进行生成。但是在实现一个迭代器时，对于当前迭代到的路径需要我们自行记录，可以采用更简便的语法生成器
    生成器是一类特殊的迭代器

2. 为什么要有生成器
列表所有数据都在内存中，如果有海量数据的话将会非常耗内存。
如：仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
如果列表元素按照某种算法推算出来，那我们就可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list，从而节省大量的空间。
简单一句话：我又想要得到庞大的数据，又想让它占用空间少，那就用生成器！


:Author: kylin
:Last Modified by: kylin.smq@qq.com
"""

# 创建生成的方法1
# 把列表生成式的[]改成()，就创建了一个generator
L = [x * 2 for x in range(10)]
nums = (x * 2 for x in range(10))
print(type(L))
print(type(nums))


# 如果一个函数中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。
# 调用函数就是创建了一个生成器（generator）对象。
def create_num(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        yield a
        a, b = b, a+b
        current_num += 1
    return "ok..."


def create_num2(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        y = yield a
        print(f">>>ret>>>{y}")
        a, b = b, a+b
        current_num += 1
    return "ok..."


# 调用函数时，就时创建了一个生成器
obj = create_num(10)
# 可用next()调用生成器对象来取值。next 两种方式 t.__next__()  |  next(t)。
# for num in obj:
#     print(num)
# 可用for 循环获取返回值（每执行一次，取生成器里面一个值）
# （基本上不会用next()来获取下一个返回值，而是直接使用for循环来迭代）。
print(obj.__next__())
print(next(obj))
# 推荐使用下方这种安全的方法
while True:
    try:
        ret = next(obj)
        print(ret)
    except StopIteration as e:
        # 输出生成器函数的return返回值
        print(e.value)
        break

# 通过send启动生成器，支持传参数
obj2 = create_num2(10)
print(next(obj2))
# send不能放在第一句
obj2.send('aaa')
print(next(obj2))
# print(obj.send(None))



