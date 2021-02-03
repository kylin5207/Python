# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
import seaborn as sns

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = [u'Arial Unicode MS']


def calc_pearson(x, y):
    """
    相关系数 = cov(X, Y) / （X标准差 * Y标准差）
    :param x:
    :param y:
    :return:
    """
    std1 = np.std(x)
    std2 = np.std(y)
    # np.sqrt(np.mean(x**2) - np.mean(x)**2)
    cov = np.cov(x, y, bias=True)
    plotCov(cov)

    covNum = cov[0, 1]
    print("cov : ", cov)

    return covNum / (std1 * std2)


def plotCov(cov):
    """
    相关系数矩阵的绘制
    :param cov:
    :return:
    """
    fig = plt.figure("Correlation Figure")
    tickLabels = ["X", "Y"]
    sns.heatmap(cov, annot=True, square=True, cmap="Blues", fmt=".3f", xticklabels=tickLabels, yticklabels=tickLabels)
    plt.title("Correlation Figure")


def intro():
    """
    利用x生成y
    :return:
    """
    N = 10
    x = np.random.rand(N)
    y = 2 * x + np.random.randn(N) * 0.1
    print(x)
    print(y)
    print('系统计算：', stats.pearsonr(x, y)[0])
    print('手动计算：', calc_pearson(x, y))


def rotate(x, y, theta=45):
    data = np.vstack((x, y))
    # print data
    mu = np.mean(data, axis=1)
    mu = mu.reshape((-1, 1))
    # print mu
    data -= mu
    # print data
    theta *= (np.pi / 180)
    c = np.cos(theta)
    s = np.sin(theta)
    m = np.array(((c, -s), (s, c)))
    return m.dot(data) + mu


def pearson(x, y, tip):
    # 颜色条
    clrs = list('rgbmycrgbmycrgbmycrgbmyc')

    plt.figure(figsize=(10, 8), facecolor='w')

    for i, theta in enumerate(np.linspace(0, 90, 6)):
        xr, yr = rotate(x, y, theta)
        p = stats.pearsonr(xr, yr)[0]
        # print calc_pearson(xr, yr)
        print('旋转角度：', theta, 'Pearson相关系数：', p)
        str = 'correlation : %.3f' % p
        plt.scatter(xr, yr, s=40, alpha=0.9, linewidths=0.5, c=clrs[i], marker='o', label=str, edgecolors='k')

    plt.legend(loc='upper left', shadow=True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Pearson And Distribution:%s' % tip, fontsize=18)
    plt.grid(b=True, ls=':', color='#404040')
    plt.show()


if __name__ == '__main__':
    # warnings.filterwarnings(action='ignore', category=RuntimeWarning)
    np.random.seed(0)

    intro()

    N = 1000
    # tip = '一次函数关系'
    # x = np.random.rand(N)
    # y = np.zeros(N) + np.random.randn(N)*0.001

    # tip = u'二次函数关系'
    # x = np.random.rand(N)
    # y = x ** 2 + np.random.randn(N)*0.002

    # tip = u'正切关系'
    # x = np.random.rand(N) * 1.4
    # y = np.tan(x)

    # # 二次函数
    # tip = u'Quadratic Function'
    # x = np.linspace(-1, 1, 101)
    # y = x ** 2

    tip = u'椭圆'
    x, y = np.random.rand(2, N) * 60 - 30
    y /= 5
    idx = (x**2 / 900 + y**2 / 36 < 1)
    x = x[idx]
    y = y[idx]

    pearson(x, y, tip)
