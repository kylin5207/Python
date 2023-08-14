"""
使用 * 将元组/列表/集合解析成多个参数传入函数
"""

def my_func(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

my_tuple = (1, 2, 3)
my_func(*my_tuple)  # 输出：a = 1, b = 2, c = 3

# 使用 * 将列表解析成多个参数传入函数
my_list = [4, 5, 6]
my_func(*my_list)   # 输出：a = 4, b = 5, c = 6

# 使用 * 将集合解析成多个参数传入函数
my_set = {7, 8, 9}
my_func(*my_set)    # 输出：a = 7, b = 8, c = 9
