def outer():
    def inner():
        print("我是内部函数")

    return inner  # 注意：返回的是 inner，没有括号！

def main():
    my_func = outer()  # outer() 执行后返回了 inner 函数
    my_func()           # 现在可以调用了

if __name__ == "__main__":
    main()