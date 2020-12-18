# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
泊松分布
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.random.poisson(lam=5, size=1000)
    pillar = 15

    plt.hist(x, bins=pillar, density=True, range=[0, pillar], color='g', edgecolor='k', alpha=0.8)
    plt.title(r'$y = \frac{\Lambda^k}{k!}e^{-\Lambda}$')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()