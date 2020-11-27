# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
大文件读取
read()默认会把文件的所有内容一次性读取到内存，
如果文件太大，对内存的占用会非常严重。

readline()一次读取一行，执行后，指针会移动到下一行，准备再次读取
"""
with open("a.txt", "r") as file:

    while True:
        text = file.readline()
        if not text:
            break

        print(text, end="")

