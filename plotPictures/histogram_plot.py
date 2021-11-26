# -*- coding:utf-8 -*-
"""
histogram_plot 直方图绘制
"""
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_NUM = 10000
BINS = 10
LOWER = 0
UPPER = 10000

data = np.random.uniform(0, 10000, (SAMPLE_NUM, ))


# h, bin_edges = np.histogram(data, BINS, range=(LOWER, UPPER))
# print(h)
# print(bin_edges)
width = SAMPLE_NUM / BINS
frequency_each, bins, _ = plt.hist(data, bins=BINS, color='deepskyblue', edgecolor='k')
print(bins[1:])
print(bins[1:] + (width // 2))
# 注意：返回值的bins的数据长度比频数的长度大1，这里推荐使用从1开始直到bins结束，即将第0个元素去掉，保证二者的长度一致，当然还需要减去width的一半，保证在中点。
plt.plot(bins[1:]-(width // 2), frequency_each, color='palevioletred', linewidth=2) # 利用返回值来绘制区间中点连线
plt.xlabel("scores")
plt.ylabel("frequency")
plt.title("Data histogram plot")
plt.show()