"""
运行时间统计
python中的timeit（）方法， 它用于获取代码的执行时间。
该库将代码语句运行一百万次，并提供从集合中花费的最短时间。这是一种有用的方法，有助于检查代码的性能。

使用方法：timeit.timeit(stmt, setup, timer, number)
参数分析：
· stmt：这将采用您要测量其执行时间的代码， string格式。默认值为“pass”。
· setup：这将包含需要在stmt之前执行的设置详细信息。默认值为“ pass”。
· timer：它将具有计时器值，timeit（）已经设置了默认值，我们可以忽略它。
· number：stmt将按照此处给出的编号执行。默认值为1000000。
"""

import timeit
import numpy as np
import random

# 查看默认时间
print(timeit.default_timer())


# timeit.repeat（stmt，setup，timer，repeat，number）
# 与timeit（）相同，但是随着重复，repeat被称为重复次数。
import_module = "import random"
testcode = '''def test():return random.randint(10, 100)'''
print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))


timing_number = 10
timing_repeat = 10
unoptimized = (
    np.array(timeit.Timer(lambda: testcode).repeat(repeat=timing_repeat, number=timing_number)) * 1000 / timing_number
)
# 帮助解释CPU噪声，我们在多个批次中多次重复运行计算，然后收集一些关于均值、中值和标准差的基础统计数据。
unoptimized = {
    "mean": np.mean(unoptimized),
    "median": np.median(unoptimized),
    "std": np.std(unoptimized),
}
#
print(unoptimized)