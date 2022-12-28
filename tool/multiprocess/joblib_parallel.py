import time
from joblib import Parallel, delayed

def run(fn):
    # fn: 函数参数是数据列表的一个元素
    time.sleep(1)
    return fn * fn

if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]
    results = []
    print('======串行执行开始======')  # 顺序执行(也就是串行执行，单进程)
    s = time.time()
    for fn in testFL:
        results.append(run(fn))
    t1 = time.time()
    print(f"串行执行时间 = {t1 - s}s")
    print(f"results = {results}")

    print("======多进程开始======")  # 创建多个进程，并行执行
    # results = []
    # 创建parallel_obj对象
    parallel_obj = Parallel(n_jobs=-1, verbose=100, backend='loky', timeout=10)
    # 开始调用被并行计算的函数,并给出结果; 实现方式为 调用内置的 __call__方法
    out = parallel_obj(delayed(run)(i) for i in testFL)
    t2 = time.time()
    print(f"并行执行时间 = {t2 - t1}s")
    print(out)


