# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
竖直条形图
plt.bar(x, height, width=0.8, bottom=None,
        ***, align='center', data=None, **kwargs)
x : x坐标
height : 条形图的高度
width : 宽度 （默认0.8）
bottom : 条形的起始位置
align : 条形的中心位置

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def main():
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.arange(0, 10, 0.1)
    y = np.sin(x)

    plt.bar(x, y, width=0.04, lw=0.2)
    plt.plot(x, y, 'r--', linewidth=2)
    plt.xlabel("y", fontsize=16)
    plt.ylabel("x", fontsize=16)
    plt.title(r"$y = sin(x)$")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()