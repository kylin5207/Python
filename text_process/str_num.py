"""
字符数值型函数
pd.to_numeric()方法，它虽然不是 str 对象上的方法，但是能够对字符格式的数值进行快速转换和筛选。
其主要参数包括 errors 和 downcast 分别代表了非数值的处理模式和转换类型。
其中，对于不能转换为数值的有三种 errors 选项， raise, coerce, ignore 分别表示直接报错、设为缺失以及保持原来的字符串。
"""
import pandas as pd

s = pd.Series(['1', '2.2', '2e', '??', '-2.1', '0'])
# 忽略无法转换的字符串
data = pd.to_numeric(s, errors="ignore")
print("====ignore=====")
print(data)

# 设为缺失
data = pd.to_numeric(s, errors="coerce")
print("====coerce=====")
print(data)

# 在数据清洗时，可以利用 coerce 的设定，快速查看非数值型的行
print(s[pd.to_numeric(s, errors='coerce').isna()])

