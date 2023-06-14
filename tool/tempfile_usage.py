"""
tempfile的使用
tempfile 模块提供了临时文件和目录的创建和管理功能。它允许您在程序运行时创建临时文件或目录，以便在处理临时数据或需要临时存储文件时使用。

"""
import pandas as pd
from sklearn.datasets import load_iris
import os
import tempfile
import time

iris = load_iris(as_frame=True)
data = pd.concat([iris.data, iris.target], axis=1)
print(data)

# 创建临时目录, 您可以在该目录中进行文件的读写操作。
with tempfile.TemporaryDirectory() as temp_dir:
    temp_path = os.path.join(temp_dir, 'iris.csv')

    # temp_path = 'iris.csv'
    data.to_csv(temp_path, index=False)
    print(f"save over, at {temp_path}")