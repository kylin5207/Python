# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
排列组合常用方法
"""
from scipy.special import perm
from scipy.special import comb
from scipy.special import factorial

# 排列数计算使用perm
# Ani = (n!)/(n-i)!
p = perm(5, 2)
print("A52排列：", p)

# 组合数计算使用comb
combination = comb(5, 2)
print("C52组合：", combination)

# 阶乘计算
factor = factorial(5)
print("5! = ", factor)

