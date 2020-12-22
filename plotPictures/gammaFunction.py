# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.special import gamma
from scipy.special import factorial

"""
gamma函数:
gamma(n) = (n-1)!
"""


def main():
    mpl.rcParams['font.sans-serif'] = [u'Arial Unicode MS']
    mpl.rcParams['axes.unicode_minus'] = False

    gamma_data = gamma(1.5)
    print(gamma_data)
    N = 5
    x = np.linspace(0, N, 50)
    y = gamma(x+1)
    plt.figure(facecolor='w')
    plt.plot(x, y, 'r-', x, y, 'ro', linewidth=2, markersize=6, mec='k')

    z = np.arange(0, N+1)
    f = factorial(z, exact=True)
    print(f)
    plt.plot(z, f, 'go', markersize=6, markeredgecolor='k')
    plt.grid(b=True, ls=':', color="#404040")
    plt.xlim(-0.1, N + 0.1)
    plt.title("gamma函数和阶乘函数的比较")
    plt.show()


if __name__ == "__main__":
    main()