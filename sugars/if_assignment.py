"""
关于if的语法糖
"""

# 带有 if 选择的条件赋值，其形式为 value = a if condition
voice = "miao"
value = "cat" if "miao".__eq__(voice) else "dog"
print(value)


# 截断列表中超过5的元素，即超过5的用5代替，小于5的保留原来的值
L = [1, 2, 3, 4, 5, 6, 7]
L = [i if i <= 5 else 5 for i in L]
print(L)
