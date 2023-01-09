"""
查看由numpy数组创建的pandas.Dataframe的内存占用
"""
from memory_profiler import profile
import numpy as np
import pandas as pd

@profile
def memory_check_1d():
    a = np.arange(int(1e6))
    a_min = a.min()
    df = pd.DataFrame(a, columns=["array"])
    df_min = df.min()
    del a
    del df

@profile
def memory_check_1d_plus():
    a = np.arange(int(1e6))
    a.flags["WRITEABLE"] = False
    a_min = a.min()
    df = pd.DataFrame(a, columns=["array"], copy=False)
    df_min = df.min()
    del a
    del df

@profile
def memory_check_2d():
    a_2d = np.random.random((int(1e6),7))
    a_2d_min = a_2d.min()
    df = pd.DataFrame(a_2d, columns=list('abcdefg'))
    df_min = df.min()
    del a_2d
    del df

@profile
def memory_check_2d_plus():
    a_2d = np.random.random((int(1e6),7))
    a_2d.flags["WRITEABLE"] = False
    a_2d_min = a_2d.min()
    df = pd.DataFrame(a_2d, columns=list('abcdefg'), copy=False)
    df_min = df.min()
    del a_2d
    del df

memory_check_1d()
memory_check_1d_plus()
memory_check_2d()
memory_check_2d_plus()

