"""
send的用法

"""

def fun_yield():
    print("starting fun yield")
    while True:
        res = yield 4

        print("判断yield之后是否继续执行", res)


g = fun_yield()  # 调用这个函数只是会得到一个生成器
print("函数结果是一个生成器：", g)

print("对此生成器还是进行调用：")
print("*******1*********")
print(next(g))
print("*******2*********")
print("生成器的返回值", g.send(1))
print("******3*********")
print("生成器的返回值", g.send(2))
print("******4**********")
print("生成器的返回值", g.send(3))
