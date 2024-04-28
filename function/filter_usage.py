"""
过滤函数filter
- 在Python中，filter函数是一个很有用的内置函数，用来从序列中筛选出符合条件的元素。
    filter(function, iterable)
    这个函数接收两个参数：一个函数和一个序列。
    提供的function函数用于定义筛选标准，返回布尔值（True或False），决定每个元素是否保留。
- 这个函数非常适合用于需要对数据进行预处理的情况，如数据清洗、数据验证等场景。
"""
# 定义一个检查数字是否为偶数的函数
def is_even(num):
    return num % 2 == 0

# 创建一个数字列表
numbers = [1, 2, 3, 4, 5, 6]

# 使用filter函数筛选偶数
# filter函数返回的是一个迭代器，因此通常需要使用list()、set()等函数转换为相应的数据结构。
even_numbers = list(filter(is_even, numbers))

print(even_numbers)
