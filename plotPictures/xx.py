# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
绘制y=x^x

"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def f(x):
    """
    如果x>0,则计算x的x方
    如果x<0,则计算-x的-x方
    :param x:
    :return:
    """
    y = np.ones_like(x)
    i = x > 0
    y[i] = np.power(x[i], x[i])
    i = x < 0
    y[i] = np.power(-x[i], -x[i])
    return y


def main():
    x = np.linspace(-1.5, 1.5, 300)
    y = f(x)
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.plot(x, y)
    plt.xlabel("x", fontsize=16)
    plt.ylabel("y", fontsize=16)
    plt.title(r'$y = x ^ x $')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()