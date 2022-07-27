"""
正则表达式
"""
import re

# 使用re.findall(正则表达式，待匹配文本)
print(re.findall(r'Apple', 'Apple! This Is an Apple!'))

# .表示匹配除换行符以外的任意字符
print(re.findall(r'.', 'abc'))

# []表示匹配方括号中包含的任意字符。
print(re.findall(r'[ac]', 'abc'))

# [^]表示匹配方括号中不包含的任意字符。
print(re.findall(r'[^ac]', 'abc'))

# {n}指匹配n次
print(re.findall(r'[abcde]{2}', 'aaaabbbbccdeeeee'))

# |分支结构，匹配符号之前的字符或后面的字符
print(re.findall(r'aaa|bbb', 'aaaabbbb'))

# \表示转义，还原元字符原来的含义；|分支结构
print(re.findall(r'a\\?|a\*', 'aa?a*a'))

# ?表示出现零次或一次
print(re.findall(r'a?.', 'abaacadaae'))

# .表示匹配除换行符以外的任意字符， s表示任意字符
print(re.findall(r'.s', 'Apple! This Is an Apple!'))

# \w匹配所有字母、数字、下划线, {2}表示至少出现2次
print(re.findall(r'\w{2}', '09 8? 7w c_ 9q p@'))

# \w匹配所有字母、数字、下划线, \W匹配非字母、数字、下划线的字符， \B匹配一组非空字符开头或结尾的位置,不代表具体字符
print(re.findall(r'\w\W\B', '09 8? 7w c_ 9q p@'))

# .表示匹配除换行符以外的任意字符, \s匹配空格符
print(re.findall(r'.\s.', 'Constant dropping wears the stone.'))

# {n,m}至少出现n次，至多出现m次；(xyz)字符组，按照确定的顺序匹配；\d匹配数字；+匹配前面的子表达式一次或多次
print(re.findall(r'上海市(.{2,3}区)(.{2,3}路)(\d+号)', '上海市黄浦区方浜中路249号 上海市宝山区密山路5号'))


