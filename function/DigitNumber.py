# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
计算一个正整数的位数
"""
import math


def main():
    n = int(input("输入正整数："))
    nums = int(math.log10(n)) + 1
    print("正整数个数 = ", nums)


if __name__ == "__main__":
    main()