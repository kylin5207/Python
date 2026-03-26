"""
手动实现装饰器
"""
def say_hello():
    print("say_hello func running")
    print("你好")

def add_logging(func):
    """接收一个函数，返回一个加了日志的新函数"""
    def wrapper():
        print("====函数开始执行===")
        func()                   # 调用原来的函数
        print("===函数执行完毕===")
    return wrapper               # 返回新函数

# 用 add_logging "装饰" say_hello
say_hello = add_logging(say_hello)

# 现在调用 say_hello，会自动带上日志
say_hello()