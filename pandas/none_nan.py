"""
· 在python中的缺失值用 None 表示，该元素除了等于自己本身之外，与其他任何元素不相等：
· 在numpy中利用np.nan来表示缺失值，该元素除了不和其他任何元素相等之外，和自身的比较结果也返会False
· 在时间序列的对象中， pandas 利用 pd.NaT 来指代缺失值，它的作用和 np.nan 是一致的
  为什么要引入 pd.NaT 来表示时间对象中的缺失呢？ 仍然以 np.nan 的形式存放会有什么问题？
  在 pandas 中可以看到 object 类型的对象，而 object 是一种混杂对象类型，如果出现了多个类型的元素同时存储在 Series 中，它的类型就会变成 object 。
  NaT 问题的根源来自于 np.nan 的本身是一种浮点类型，而如果浮点和时间类型混合存储，如果不设计新的内置缺失类型来处理，就会变成含糊不清的 object 类型，这显然是不希望看到的。
"""
import numpy as np
import pandas as pd

print(None == None)
print(1 == None)
print(None == [])

print("====np.nan=====")
print(np.nan == np.nan)
print(np.nan == None)
print(np.nan == False)
# numpy.nan是一个浮点数
print(f"np.nan type = {type(np.nan)}")

# 值得注意的是，虽然在对缺失序列或表格的元素进行比较操作的时候，np.nan 的对应位置会返回 False，
# 但是在使用 equals 函数进行两张表或两个序列的相同性检验时，会自动跳过两侧表都是缺失值的位置，直接返回 True
s1 = pd.Series([1, np.nan])
s2 = pd.Series([1, 2])
s3 = pd.Series([1, np.nan])
print(s1 == 1)
print(s1.equals(s2))
print(s1.equals(s3))

# 在时间序列的对象中， pandas 利用 pd.NaT 来指代缺失值，它的作用和 np.nan 是一致的
print(pd.to_timedelta(['30s', np.nan])) # Timedelta中的NaT)
