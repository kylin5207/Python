# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
胸型线绘图
y = a(-3xlog(x)+e^b)
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def main():
    x = np.arange(1, 0, -0.001)
    y = (-3 * x * np.log(x) + np.exp(-(40 * (x - 1 / np.e)) ** 4) / 25) / 2
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    plt.plot(y, x, 'r-', linewidth=2)
    plt.xlabel("y", fontsize=16)
    plt.ylabel("x", fontsize=16)
    plt.title(r"$y = a(-3xlog(x)+e^b)$")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()