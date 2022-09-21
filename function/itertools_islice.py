"""
fibnacci高阶实现
"""
import itertools

a, b = 17, 55

print("=====initial data====")
print(f"{a = }, {b = }")

# 元素交换
a, b = b, a
print("=====After swap====")
print(f"{a = }, {b = }")

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

# itertools.islice(iterable, start, stop)，返回迭代器中start到stop的位置
# 从迭代器中获得前12个元素
print(list(itertools.islice("ABCD", 2)))
print(list(itertools.islice(fib(), 12)))