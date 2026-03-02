import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")  # 或者 "Qt5Agg"

# macOS 中文字体路径
myfont = font_manager.FontProperties(fname="/System/Library/Fonts/Supplemental/Arial Unicode.ttf")

sns.set_style("whitegrid")

# 加载数据
data_path = "../data/bank_marketing/bank/bank-full.csv"
df = pd.read_csv(data_path, sep=';')  # CSV 使用分号分隔

month_order = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
month_counts = df['month'].value_counts().reindex(month_order)

plt.figure(figsize=(12,6))
sns.barplot(x=month_counts.index, y=month_counts.values, color='#1f77b4')

# 设置中文标签和标题
plt.xlabel("月份", fontproperties=myfont, fontsize=12)
plt.ylabel("客户数量", fontproperties=myfont, fontsize=12)
plt.title("Bank Marketing: 每月客户数量分布", fontproperties=myfont, fontsize=16)


plt.show()