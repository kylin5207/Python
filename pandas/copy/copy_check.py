import pandas as pd
import numpy as np
import copy

data = pd.DataFrame([[1, 2], [3, 3]], columns=["A", "B"])
s = pd.Series([1, 2], index=["a", "b"])

# 深拷贝，默认进行深拷贝
data_deep = data.copy()
s_deep = s.copy()
# copy.deepcopy(data)
print(f"====deep copy=====")
print(f"(DataFrame) index and values is same object? {data_deep.index is data.index and data_deep.values is data.values}")
print(f"(Series) index and values is same object? {s_deep.index is s.index and s_deep.values is s.values}")
print(f"(DataFrame) index object is same object? {data_deep.loc[0] is data.loc[0]}")

data_shallow = data.copy(deep=False)
s_shallow = s.copy(deep=False)
print(f"====shallow copy=====")
print(f"(DataFrame)index and values is same object? {data_shallow.index is data.index and data_shallow.values is data.values}")
print(f"(Series) index and values is same object? {s_shallow.index is s.index and s_shallow.values is s.values}")
print(f"(DataFrame) index object is same object? {data_shallow.loc[0] is data.loc[0]}")

# change item
print("change item")
print("=====Before=====")
print(data)
data.loc[0][1] = 1000
print("=====After=====")
print(data)
print("====deep======")
print(data_deep)
print("====shallow======")
print(data_shallow)


a = np.array([1, 2, 1, 1])
b = np.array([2, 2, 2, 2])
data = pd.DataFrame([a, b])
print("====data======")
print(data)
data_deep = data.copy()
print("====deep======")
print(data_deep)
data.loc[0][1] = 1000
print(data)
print(data_deep)

print("=======inner copy=======")
df1 = pd.DataFrame({'A':[[1,2],[3,4],[5,6]],'B':[[7,8],[9,10],[11,12]]})
df2 = df1.copy(deep=True)
df3 = copy.deepcopy(df1)

print("=====Before=====")
print(df1)

print("=====After=====")
df1.iloc[0,0][0] = 999

print("initial data")
print(df1)
print("pandas.DataFrame.copy")
print(df2)
print("copy.deepcopy")
print(df3)
# 因为我仅仅对dataframe进行了深拷贝，因此我得到了一个新的dataframe，该dataframe和原来的dataframe一样，每个元素存储的都是list的引用，
# 注意是list的引用而不是list，因此我实际上是深拷贝了list的引用，但是并不是把里面的数据都拷贝了一遍。
# 当我修改深拷贝过来的dataframe中的list中的元素时，我是真正的改掉了list中的元素，因此原来的dataframe和深拷贝的dataframe中的每个元素的引用中的元素都被改掉了，
# 这就是出现上述现象的原因。