import pandas as pd
import numpy as np

data = pd.DataFrame({"X": [0, 25, 50, 75, 100]})
print(data)

# 等距分箱pandas.cut
# X的范围在每一侧扩展了1%，以包括X的最小值和最大值。
# 参数：
#   - X: 数据(必须1维)
#   - bins: 分箱数
#   - right(True): 生成区间为左开右闭区间
#   - labels:
#         False: 返回X对应的分箱结果
#   - retbins(False):
#         是否需要返回分箱节点
#   - duplicates: drop 删除重复边缘
print("=====等距分箱======")
# 最后返回分箱后的数据，以及对应的分裂点（注意分裂点的个数为bins+1）
X_bin, split_points = pd.cut(data["X"], bins=4, labels=False, retbins=True, duplicates="drop")
print("======data after binning======")
print(X_bin)
print("=====split_points=====")
print(split_points)


# 等频分箱pandas.qcut
# 参数：
#   - X: 数据(必须1维)
#   - q: int或float列表，例如[0, .25, .5, .75, 1.]
#   - labels:
#         False: 返回X对应的分箱结果
#   - precision(3): 精度
#   - retbins(False):
#         是否需要返回分箱节点
#   - duplicates: drop 删除重复边缘
print("=====等频分箱======")
X_bin, split_points = pd.qcut(data["X"], q=4, labels=False, retbins=True, duplicates="drop")
print(X_bin)
print(split_points)

