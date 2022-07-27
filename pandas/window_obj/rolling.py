"""
pandas中的窗口对象：滑动窗口 rolling 、扩张窗口 expanding 以及指数加权窗口 ewm
"""
import pandas as pd

# 要使用滑窗函数，就必须先要对一个序列使用.rolling()得到滑窗对象
# 其最重要的参数为窗口大小 window
s = pd.Series([1,2,3,4,5])
s_roller = s.rolling(window=3)
# 其返回值为一个Rolling对象
print(s_roller)

# 得到滑动对象后，能够使用相应的聚合函数进行计算
# 需要注意的是窗口包含当前行所在的元素
print("=== mean ====")
print(s_roller.mean())
print("=== sum ====")
print(s_roller.sum())

# 协方差和相关系数
s2 = pd.Series([1,2,6,16,30])
print("=== cov ====")
print(s_roller.cov(s2))
print("=== corr ====")
print(s_roller.corr(s2))

# 此外，还支持使用 apply 传入自定义函数，其传入值是对应窗口的 Series
print("=== apply mean ====")
print(s_roller.apply(lambda x:x.mean()))

# shift, diff, pct_change 是一组类滑窗函数，它们的公共参数为 periods=n ，默认为1，
# 分别表示偏移n个元素的值、与向前第n个元素做差(与 Numpy 中不同，后者表示做差的间隔)、与向前第n个元素相比计算增长率。
# 这里的n可以为负，表示反方向的类似操作。
# 将其视作类滑窗函数的原因是，它们的功能可以用窗口大小为 n+1 的 rolling 方法等价代替
s = pd.Series([1,3,6,10,15])
print("===initial Series==")
print(s)

print("===shift with 2===")
# shift(n)偏移n个元素
print(s.shift(2))
print("===shift with -1===")
print(s.shift(-1))

print("===diff with 3===")
# diff(3)进行3阶差分计算
print(s.diff(3))

print("===pct_change===")
print(s.pct_change())


