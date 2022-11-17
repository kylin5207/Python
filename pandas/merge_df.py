import numpy as np
import pandas as pd
"""
pandas.merge()在两个数据集合并时，可以指定不同的列名，left_on="xxx", right_on="xxx"
left_on为第一个参与方的id，right_on为第二个参与方的id
"""

# 合并的key相同
data1 = pd.DataFrame({"id":np.array([1, 2, 3]), "y":np.array([1, 0, 1], dtype=int), "x1": np.array([0.1, 0.2, 0.1]), "x2": np.array([0.2, 0.3, 0.5])})
data2 = pd.DataFrame({"id":np.array([2, 3, 6]), "x3": np.array([0.1, 0.2, 0.1]), "x4": np.array([0.2, 0.3, 0.5])})
print("====data1=====")
print(data1)
print("====data2=====")
print(data2)

# merge
merge_df = pd.merge(data1, data2, left_on="id", right_on="id")
print("====merge on {id}=====")
print(merge_df)

# 如果两边参与方的id名不一致
data3 = pd.DataFrame({"ID":np.array([1, 3, 6]), "x5": np.array([0.1, 0.2, 0.1]), "x6": np.array([0.2, 0.3, 0.5])})
print("====data3=====")
print(data3)

# 合并后，会有两列值相同的id
merge_df = pd.merge(data1, data3, left_on="id", right_on="ID")
print("====merge on {id, ID}=====")
print(merge_df)
# 这时候需要手动删除一列id
