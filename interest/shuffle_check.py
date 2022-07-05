import numpy as np
import random
"""
shuffle对比
此时，可以认为random.shuffle()内部的实现机制是不兼容numpy数组，
· 对于numpy数组的shuffle尽可能用numpy.random.shuffle()
· 对于list数据用random.shuffle()。
"""
# 数据换位
# 对于numpy元素直接利用行号进行换位的方式是错误的
data1 = np.array([[1,1,1], [2,2,2], [3,3,3]])
# data2 = np.array([[1,1,1], [2,2,2], [3,3,3]])
# 地址可能重了，发现真的一样
print("****numpy*****")
print("===Before===")
print(f"data1[0] = {id(data1[0])}")
print(f"data1[0] = {id(data1[0])}")
print(f"data1[2] = {id(data1[2])}")
print(f"data1 = {id(data1)}")
print(data1[0].__array_interface__['data'])
print(data1[1].__array_interface__['data'])

data1[0], data1[2] = data1[2], data1[0]
print("===After===")
print(f"data1[0] = {id(data1[0])}")
print(f"data1[2] = {id(data1[2])}")
print(f"data1 = {id(data1)}")

# 对于list元素，可以利用索引进行换位
# a = [1, 2, 3, 4]
# a[0], a[1] = a[1], a[0]
# print(a)
data2 = [[1,1], [2,2], [3,3]]
print("****list*****")
print("===Before===")
print(f"data2[0] = {id(data2[0])}")
print(f"data2[2] = {id(data2[2])}")
print(f"data2 = {id(data2)}")

data2[0], data2[1] = data2[1], data2[0]
print("===After===")
print(f"data2[0] = {id(data2[0])}")
print(f"data2[2] = {id(data2[2])}")
print(f"data2 = {id(data2)}")

# 一维元素均能进行正常的shuffle
# data1 = np.array([1,2,2,4,3])
# data2 = np.array([1,2,2,4,3])
# 多维numpy数组就有问题
# data1 = np.array([[1,1,1], [2,2,2], [3,3,3]])
# data2 = np.array([[1,1,1], [2,2,2], [3,3,3]])
print("===numpy.random.shuffle=====")
print("Before")
print(data1)
np.random.seed(0)
np.random.shuffle(data1)
print("After")
print(data1)

# random.shuffle()用于将一个列表中的元素打乱顺序，值得注意的是使用这个方法不会生成新的列表，只是将原列表的次序打乱
print("===random.shuffle=====")
print("Before")
print(data2)
random.seed(0)
random.shuffle(data2)
print("After")
print(data2)
