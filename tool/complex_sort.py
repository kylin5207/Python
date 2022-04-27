"""
较为复杂的排序

当遇到较为复杂的排序的时候，利用cmp_to_key实现～
    cmp_to_key在内部定义了一个类K， 并使用我传入的cmp比较函数完成了比较关系运算符的重载，函数返回的是一个类，
    而sort函数的key需要的是一个函数，看起来矛盾，但在python中，这样做完全可行，因为类和函数都是callable的，这里把类当成了函数来用。

"""
from functools import cmp_to_key

def cmp(x, y):
    """
    按照第一个元素升序排序，如果相同则按照第二个元素降序排序
    """
    if x[0] > y[0]:
        return 1
    elif x[0] < y[0]:
        return -1
    elif x[1] > y[1]:
        return -1
    else:
        return 1

intervals = [[1, 3], [2, 4], [1, 2], [1, 5]]
intervals.sort(key=cmp_to_key(cmp))
print(intervals)