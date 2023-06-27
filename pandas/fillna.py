"""
缺失值填充
"""

import pandas as pd
import numpy as np

data = np.array([[1, 2, np.nan], [20, np.nan, 40], [np.nan, 100, 200]])

data_df = pd.DataFrame(data, columns=list('abc'))
print("=====initial data====")
print(data)

# 均值填充
mean_fill = data_df.fillna(data_df.mean(skipna=True))
print(f"====mean fill====")

# 众数填充
mode_fill = data_df.fillna(data_df.mode())
print(f"======mode fill======")
print(mode_fill)

# 常数填充
fill_dict = {"a":1000, "b":2000, "c": 0}
constant_fill = data_df.fillna(fill_dict)
print(f"==== constant fill =====")
print(constant_fill)

# 中位数填充
median_value = data_df.median(skipna=True)
median_fill = data_df.fillna(median_value)
print(f"==== median fill =====")
print(median_fill)

# 如果想对numpy.ndarray用中位数填充缺失值
median_fill = np.nanmedian(data, axis=0)


