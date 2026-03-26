
def outer():
    print("--我是外部函数--")

    def inner():
        print("--我是内部函数--")

    inner()  # 在外部函数里调用内部函数

def main():
    outer()

if __name__ == '__main__':
    main()