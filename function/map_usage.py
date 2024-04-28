"""
映射函数map
- 在Python中，map函数是一种内置函数，它可以将一个函数应用于一个序列（如列表、元组）的每个元素，
    然后返回一个迭代器，其中包含应用函数后的结果。
    map(function, iterable, ...)
- map是处理数据和进行批量转换的一种非常有用的方法，特别是在需要对每个元素执行相同操作的场景中
"""
# 定义一个加10的函数
def add_ten(x):
    return x + 10

# 创建一个数字列表
numbers = [1, 2, 3, 4, 5]

# 使用map函数处理每个元素
# map函数返回的是一个迭代器，这意味着它是惰性求值的，只有在迭代时才会计算。因此，通常需要使用list()、set()等函数来获取所有结果。
result = list(map(add_ten, numbers))

print(result)