import time
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor

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
    results = []
    with Pool(3) as p:
        for fn in testFL:
            results.append(p.apply_async(run, (fn,)))
        p.close() # 关闭进程池，不再接受新的进程
        p.join() # 主进程阻塞等待子进程的退出
    t2 = time.time()
    print(f"并行执行时间 = {t2 - t1}s")
    for res in results:
        print(res.get())


