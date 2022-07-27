"""
插值
对于 interpolate而言，除了插值方法（默认为 linear 线性插值）之外，
有与 fillna 类似的两个常用参数，一个是控制方向的 limit_direction ，另一个是控制最大连续缺失值插值个数的 limit 。
其中，限制插值的方向默认为 forward ，这与 fillna 的 method 中的 ffill 是类似的，若想要后向限制插值或者双向限制插值可以指定为 backward 或 both 。
"""

import pandas as pd
import numpy as np

s = pd.Series([np.nan, np.nan, 1,
               np.nan, np.nan, np.nan,
               2, np.nan, np.nan])
print("===initial data====")
print(s)

# 使用fillna插值
# 在 fillna 中有三个参数是常用的： value, method, limit 。
# 其中， value 为填充值，可以是标量，也可以是索引到元素的字典映射；
# method 为填充方法，有用前面的元素填充 ffill 和用后面的元素填充 bfill 两种类型，
# limit 参数表示连续缺失值的最大填充次数。
a = s.fillna(method="ffill", limit=2)
print(a)

# 使用interpolate实现
# 在默认线性插值法下分别进行 backward 和双向限制插值，同时限制最大连续条数为1
res = s.interpolate(limit_direction='backward', limit=1)
print(res)
# 最近邻插补，即缺失值的元素和离它最近的非缺失值元素一样
res = s.interpolate(method='nearest')
print(res)

# 索引插值
s = pd.Series([0,np.nan,10],index=[0,1,10])
print(s)
res1 = s.interpolate() # 默认的线性插值，等价于计算中点的值
print(res1)
res2 = s.interpolate(method='index') # 和索引有关的线性插值，计算相应索引大小对应的值
print(res2)