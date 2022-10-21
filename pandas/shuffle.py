"""
pandas 数据shuffle
"""
import numpy as np
import pandas as pd

# 生成数据
data = pd.DataFrame(np.random.randint(10, size=(10,3)), columns=list('ABC'))
print("===========  initial data =======")
print(data)

# frac指明采样的比例，我们想要实现shuffle，则把比例设置为1。
data_shuffled = data.sample(frac=1, random_state=0)
print("=====data shuffled========")
print(data_shuffled)