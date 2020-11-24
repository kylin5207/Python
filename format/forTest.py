# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS

"""
完整的for循环下方可以有一个else
这个else用于定义当程序没有break退出循环，即循环正常结束后会执行的动作
"""

nameList = ["a", "b", "c", "d"]


for name in nameList:
    if name == "c":
        break
    print(name)
else:
    print("No")
