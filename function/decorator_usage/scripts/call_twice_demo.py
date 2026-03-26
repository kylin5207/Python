def say_hello():
    print("你好")

def say_goodbye():
    print("再见")

def call_twice(func):
    """接收一个函数，调用它两次"""
    func()
    func()


def main():
    # 调用两次say_hello
    print("====say_hello=====")
    call_twice(say_hello)

    # 调用两次say_goodbye
    print("====say_goodbye=====")
    call_twice(say_goodbye)


if __name__ == '__main__':
    main()