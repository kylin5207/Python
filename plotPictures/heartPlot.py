# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
心型线:
    x = asin(t)^b
    y = c_1cos(t) - c_2cos(2t) - c_3cos(3t) - c_4cos(4t)
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def main():
    t = np.linspace(0, 7, 100)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    mpl.rcParams['font.sans-serif'] = [u'Times New Roman']
    mpl.rcParams['axes.unicode_minus'] = False

    plt.plot(x, y, 'r-', linewidth=2)
    plt.xlabel(r"$x = asin(t)^b$", fontsize=14)
    plt.ylabel(r"$y = c_1cos(t) - c_2cos(2t) - c_3cos(3t) - c_4cos(4t)$", fontsize=14)
    plt.title(u"heart plot")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()