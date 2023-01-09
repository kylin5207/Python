from memory_profiler import profile
import numpy as np
import pandas as pd

class Monk():
    @profile
    def memory_check_1d(self):
        a = np.arange(int(1e6))
        a_min = a.min()
        df = pd.DataFrame(a, columns=["array"])
        df_values = df.values
        print(f"a id = {id(a)}")
        print(f"df_values id = {id(df_values)}")
        df_min = df.min()
        del a
        del df


monk = Monk()
monk.memory_check_1d()
