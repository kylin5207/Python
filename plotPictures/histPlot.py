# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
利用均匀分布验证中心极限定理
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def main():
    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    fig = plt.figure("Central limit theorem verification", figsize=(7, 5.5))
    plt.rc('font', family='Times New Roman')
    plt.subplots_adjust(wspace=0.2, hspace=0.75)  # 调整子图间距

    # 1. 均匀分布
    x = np.random.rand(10000)
    plt.subplot(1, 2, 1)
    plt.hist(x, 30, color='m', edgecolor='k', alpha=0.5)
    plt.title("Uniform Distribution")
    plt.grid()

    # 2. 验证中心极限定理
    t = 10000
    a = np.zeros(1000)

    for i in range(t):
        a += np.random.uniform(-5, 5, 1000)

    a /= t

    plt.subplot(1, 2, 2)
    plt.hist(a, bins=30, color='g', alpha=0.5, edgecolor='k', density=True)
    plt.title(r"Normal distribution")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()