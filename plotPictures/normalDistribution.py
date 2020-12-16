# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
正态分布概率密度函数
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def main():
    mu = 0
    sigma = 1
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
    y = np.exp(- (x - mu) ** 2 / (2 * sigma ** 2)) / (np.sqrt(2 * np.pi) * sigma)
    mpl.rcParams['font.sans-serif'] = [u'Times new Roman']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.plot(x, y, 'r-o', lw=2, markersize=8)
    plt.title("Normal Distribution")
    plt.xlabel("x", fontsize=16)
    plt.ylabel("y", fontsize=16)
    plt.show()


if __name__ == "__main__":
    main()