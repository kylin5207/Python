"""
类中方法嵌套查找
"""

import time
from joblib import Parallel, delayed

class Find:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # 创建parallel_obj对象
        self.parallel_obj = Parallel(n_jobs=-1, verbose=100, backend='loky', timeout=10)

    def find_best(self, nums):
        def run(fn, a, b):
            # fn: 函数参数是数据列表的一个元素
            time.sleep(1)
            return fn**2 + a + b

        # 开始调用被并行计算的函数,并给出结果; 实现方式为 调用内置的 __call__方法
        out = self.parallel_obj(delayed(run)(i, self.a, self.b) for i in nums)
        return max(out)


if __name__ == "__main__":
    testFL = [1, 10, 3, 2, 6, 5]
    find_obj = Find(10, 20)
    t1 = time.time()
    best = find_obj.find_best(testFL)
    t2 = time.time()
    print(f"Time = {t2 - t1}s")
    print(f"best = {best}")


