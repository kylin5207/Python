import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
"""
不同的高斯函数
"""
X = np.linspace(-5, 5, 1000)

# 高斯函数1
normal_1 = multivariate_normal(mean=0, cov=1)
y_1 = normal_1.pdf(X)

# 高斯函数2
normal_2 = multivariate_normal(mean=2, cov=2)
y_2 = normal_2.pdf(X)

mix = np.max([y_1,y_2], axis=0)

plt.plot(X, mix, color='yellow', label="mixture", alpha=0.5, linewidth=10)
plt.plot(X, y_1, color='red', label="mean = 0, cov = 1")
plt.plot(X, y_2, color='blue', label="mean = 2, cov = 2")

plt.legend()
plt.title("Gaussian mixture model")
plt.show()
# plt.savefig("Gaussain_plot.png", dpi=400)