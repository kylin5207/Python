class AutoMath:
    def __getattr__(self, name):
        """
        当访问object不存在的属性时会调用该方法
        :param name:
        :return:
        """
        op, num = name.split("_")
        num = int(num)

        return {
            "times": lambda val: val * num,
            "plus": lambda val: val + num,
            "minus": lambda val: val - num,
            "dividedby": lambda val: val / num
        }[op]

if __name__ == "__main__":
    auto = AutoMath()
    print(auto.times_40(13))