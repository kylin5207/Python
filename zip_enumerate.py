"""
zip()能够把多个可迭代对象打包成一个元组构成的可迭代对象，它返回了一个zip对象.
enumerate() 是一种特殊的打包，它可以在迭代时绑定迭代元素的遍历序号
"""

# zip打包后得到的是zip对象
L1, L2, L3 = list('abc'), list('def'), list('hij')
# 可以通过list或者tuple，获得打包后的数据
print("===zip=====")
print(list(zip(L1, L2, L3)))
print(tuple(zip(L1, L2, L3)))

# 往往会在循环迭代的时候使用到zip函数
print("===zip in for loop=====")
for i, j, k in zip(L1, L2, L3):
    print(i, j, k)

# enumerate可以给迭代对象遍历序号
print("===enumerate=====")
for i, v in enumerate(L1):
    print(i, v)

# zip也可以实现
for i, v in zip(range(len(L1)), L1):
    print(i, v)

# 当利用两个列表建立字典时
my_dict = dict(zip(L1, L2))
print(my_dict)

# 解压
zipped = list(zip(L1, L2, L3))
decompress = list(zip(*zipped))
print("=== * for decompress =====")
print(decompress)
