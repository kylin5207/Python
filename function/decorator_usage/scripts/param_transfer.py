from datetime import datetime

week_map = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

def say(name):
    print(f"你好，{name}")

def add_logging(func):
    def wrapper(name):            # wrapper 也接收 name
        print("函数开始执行")
        func(name)                # 传给原函数
        print("函数执行完毕")
    return wrapper

def add_logging_optim(func):
    def wrapper(*args, **kwargs):       # 接收任意参数
        print("函数开始执行")
        result = func(*args, **kwargs)  # 原样传给原函数
        print("函数执行完毕")
        return result                   # 别忘了返回原函数的返回值
    return wrapper

@add_logging
def say(name):
    print(f"你好，{name}")

@add_logging_optim
def say_optim(name, today):
    print(f"你好，{name}, 今天是{week_map[today.weekday()]}")

def main():
    print("===单个参数用法==")
    say("zhangsan")

    print("====多个参数用法====")
    today = datetime.today()
    say_optim("zhangsan", today)

if __name__ == "__main__":
    main()