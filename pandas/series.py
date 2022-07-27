"""
Pandas DataFrame —— Series
Series 一般由四个部分组成，分别是序列的值data 、索引index 、存储类型 dtype 、序列的名字 name 。其中，索引也可以指定它的名字，默认为空。
object 代表了一种混合类型，例如存储了整数、字符串以及 Python 的字典数据结构。
此外，目前 pandas 把纯字符串序列也默认认为是一种 object 类型的序列，但它也可以用 string 类型存储。
"""
import pandas as pd

s = pd.Series(data = [100, 'a', {'dic1':5}],
              index = pd.Index(['id1', 20, 'third'], name='my_idx'),
              dtype = 'object',
              name = 'my_name')
print("=== show series ===")
print(s)
# 对于这些属性，可以通过.的方式来获取
print("=== get values ===")
print(s.values)
# 可以通过索引获取
print("=== get by index ===")
print(s[20])