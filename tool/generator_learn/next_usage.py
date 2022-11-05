import pickle_usage
import random

left = 0
right = 10
random.seed(0)

def generate():
    while True:
        print("***start**")
        yield random.randint(left, right)
        print("***end**")

# 直接调用，返回的是一个生成器对象
print(type(generate()))

# 获得生成器对象
g = generate()
# 第一次调用next，相当于启动生成器，会从生成器函数的第一行代码开始执行，直到第一次执行完yield语句后，跳出生成器函数。
print("=====1===")
print(next(g))
print("=====2===")
print(next(g))
print("=====3===")
print(next(g))
