# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
利用直方图显示正态分布
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm


def main():
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    mu = 2
    sigma = 3

    data = mu + sigma * np.random.randn(1000)

    h = plt.hist(data, 30, density=True, color="#a0a0ff", edgecolor='k')

    x = h[1]
    y = norm.pdf(x, loc=mu, scale=sigma)
    # 红色线，红色点
    # plt.plot(x, y, 'r-o', linewidth=2, markersize=4)
    # 绿色线，绿色点
    plt.plot(x, y, 'r--', x, y, 'go', linewidth=2, markersize=4)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()