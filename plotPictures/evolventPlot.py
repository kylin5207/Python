# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS

"""
渐开线的实现：
    x = tsin(t) + cos(t)
    y = sin(t) - tcos(t)
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def main():
    t = np.linspace(0, 50, 1000)
    x = t * np.sin(t) + np.cos(t)
    y = np.sin(t) - t * np.cos(t)
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    plt.plot(x, y, 'r-', linewidth=2)
    plt.xlabel(r"$x = tsin(t) + cos(t)$", fontsize=16)
    plt.ylabel(r"$y = sin(t) - tcos(t)$", fontsize=16)
    plt.title(u"evolvent plot")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()