import numpy as np
from multiprocessing import shared_memory
import pandas as pd
from memory_profiler import profile
from joblib import Parallel, delayed
import time

@profile
def write_memory_check():
    idx = np.arange(int(1e6))
    share_idx = shared_memory.SharedMemory(name='share_idx', create=True, size=idx.nbytes)
    # write memory data
    data_idx = np.ndarray(idx.shape, dtype=idx.dtype, buffer=share_idx.buf)
    data_idx[:] = idx[:]

    t1 = time.time()
    out = Parallel(n_jobs=-1, verbose=0, backend='loky')(delayed(do_func)(idx.shape[0]) for i in range(10))
    t2 = time.time()
    print(f"time = {t2 - t1}s")

    share_idx.close()
    share_idx.unlink()

@profile
def do_func(num):
    share_idx = shared_memory.SharedMemory(name='share_idx')
    shared_array = np.ndarray((num,), dtype=float, buffer=share_idx.buf)

    df = pd.DataFrame(shared_array, columns=["idx"])
    print(f"data_min = {df.min()}")
    share_idx.close()

write_memory_check()