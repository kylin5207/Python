def add_logging(func):
    """接收一个函数，返回一个加了日志的新函数"""
    def wrapper():
        print("====函数开始执行===")
        func()                   # 调用原来的函数
        print("===函数执行完毕===")
    return wrapper               # 返回新函数

@add_logging
def say_hello():
    print("say_hello func running")
    print("你好")

def main():
    say_hello()

if __name__ == '__main__':
    main()