"""
格式型函数
格式型函数主要分为两类，第一种是除空型，第二种是填充型。
1. 除空型
    其中，第一类函数一共有三种，它们分别是 strip, rstrip, lstrip ，分别代表去除两侧空格、右侧空格和左侧空格。
    这些函数在数据清洗时是有用的，特别是列名含有非法空格的时候。
2. 填充型
   pad 是最灵活的，它可以选定字符串长度、填充的方向和填充内容：
"""
import pandas as pd

# 除空
my_index = pd.Index([' col1', 'col2 ', ' col3 '])

print("====strip 两端除空====")
print(my_index.str.strip())

print("====lstrip 左端除空====")
print(my_index.str.lstrip())

print("====rstrip 右端除空====")
print(my_index.str.rstrip())

# 填充
s = pd.Series(['a','b','c'])
print("====left pad fill with 5====")
print(s.str.pad(5,'left','*'))
print(s.str.rjust(5, '*'))

print("====right pad fill with 5====")
print(s.str.pad(5,'right','*'))
print(s.str.ljust(5, '*'))

print("====both pad fill with 5====")
print(s.str.pad(5,'both','*'))
print(s.str.center(5, '*'))

