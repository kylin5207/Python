# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
插值绘制
"""
from scipy.stats import poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import scipy
import matplotlib as mpl


def main():
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.random.poisson(lam=5, size=1000)
    pillar = 15

    # 第一个返回值：每个bins点对应的频率值
    # 第二个返回值：每个bin的区间范围
    # 第三个返回值：每个bin里面包含的数据，是一个list
    a = plt.hist(x, bins=pillar, density=True, range=[0, pillar], color='g', edgecolor='k', alpha=0.8)
    plt.title(r'$y = \frac{\Lambda^k}{k!}e^{-\Lambda}$')
    plt.grid()
    plt.show()
    print(a)

    rv = poisson(5)
    x1 = a[1]
    y1 = rv.pmf(x1)
    itp = BarycentricInterpolator(x1, y1)  # 重心插值
    x2 = np.linspace(x.min(), x.max(), 50)
    y2 = itp(x2)
    cs = CubicSpline(x1, y1)       # 三次样条插值

    plt.plot(x2, cs(x2), 'm--', linewidth=5, label='CubicSpine')           # 三次样条插值
    plt.plot(x2, y2, 'g-', linewidth=3, label='BarycentricInterpolator')   # 重心插值
    plt.plot(x1, y1, 'r-', linewidth=1, label='Actural Value')             # 原始值
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()