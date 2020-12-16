# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
双坐标轴绘图：
    绘制两个或多个数据序列，他们共享一个x轴，但是y值有很大差异
"""
import pylab
import matplotlib

def main():
    """
    随着时间的推移，美国缅因州的离婚率和该国人均人造黄油消费量之间存在一种奇怪但毫无意义的相关性。
    这里的两个序列拥有不同的单位和意义，所以应在不同的y轴上绘制，共享一个共同的x轴（年）。
    :return:
    """
    years = range(2000, 2010)
    divorce_rate = [5.0, 4.7, 4.6, 4.4, 4.3, 4.1, 4.2, 4.2, 4.2, 4.1]
    margarine_consumption = [8.2, 7, 6.5, 5.3, 5.2, 4, 4.6, 4.5, 4.2, 3.7]

    matplotlib.rcParams['font.sans-serif'] = [u'Arial Unicode MS']
    matplotlib.rcParams['axes.unicode_minus'] = False
    pylab.title("Compare with the divorce rate and margarine consumption(per capita) in Maine")
    line1 = pylab.plot(years, divorce_rate, 'b-o', label="缅因州离婚率")
    pylab.ylabel("Divorce rate in Maine")

    pylab.twinx()
    line2 = pylab.plot(years, margarine_consumption, 'r-o', label="黄油消耗水平")
    pylab.ylabel("margarine consumption(per capita)")

    lines = line1 + line2
    labels = []

    for line in lines:
        labels.append(line.get_label())

    pylab.legend(lines, labels)
    pylab.show()


if __name__ == "__main__":
    main()