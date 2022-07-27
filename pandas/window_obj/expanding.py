"""
pandas中的窗口对象：扩张窗口 expanding
扩张窗口又称累计窗口，可以理解为一个动态长度的窗口，其窗口的大小就是从序列开始处到具体操作的对应位置
其使用的聚合函数会作用于这些逐步扩张的窗口上。
具体地说，设序列为a1, a2, a3, a4，则其每个位置对应的窗口即[a1]、[a1, a2]、[a1, a2, a3]、[a1, a2, a3, a4]。
"""
import pandas as pd

s = pd.Series([1, 3, 6, 10])
print("===initial data===")
print(s)

print("===expanding mean===")
print(s.expanding().mean())
# cummax, cumsum 函数是典型的类扩张窗口函数
# cumsum
print(s.expanding().sum())
# cummax
print(s.expanding().max())


