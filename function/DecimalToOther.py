# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
进制转换：
    十进制转二进制：bin()
    十进制转八进制：oct()
    十进制转十六进制：hex()
    十进制转ASCII：。
"""


def main():
    digital = int(input("输入十进制数据："))
    print("十进制->二进制： ", bin(digital))
    print("十进制->八进制：", oct(digital))
    print("十进制->十六进制：", hex(digital))
    print("十进制->ASCII：", chr(digital))
    print("ASCII->十进制：", ord('A'))


if __name__ == "__main__":
    main()