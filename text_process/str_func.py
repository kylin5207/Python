"""
字符型常用函数
"""
import pandas as pd

s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])

print("===upper====")
# upper全大写
print(s.str.upper())

print("===lower====")
# lower全小写
print(s.str.lower())

print("===title===")
# title每个单词首字母大写
print(s.str.title())

print("===capitalize====")
# capitalize，首字母大写
print(s.str.capitalize())