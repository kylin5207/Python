"""
统计型
    count和len的作用分别是返回出现正则模式的次数和字符串的长度
"""

import pandas as pd

s = pd.Series(['cat rat fat at', 'get feed sheet heat'])

# count返回出现正则模式的次数
print(s.str.count('[r|f]at|ee'))

# len返回字符串的长度
print(s.str.len())


