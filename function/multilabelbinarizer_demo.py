import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# ============================
# 示例多标签数据
# ============================
label_series = pd.Series([
    "气阴两虚证,痰瘀互结证",
    "心阳虚证,痰瘀阻络证",
    "气阴两虚证"
])

# ============================
# 多标签编码
# ============================
# 1. 拆分每条记录的标签
labels_list = label_series.str.split(',')

print(labels_list)

# 2. 使用 MultiLabelBinarizer 进行 one-hot 编码
mlb = MultiLabelBinarizer()
y_encoded = mlb.fit_transform(labels_list)

# ============================
# 输出结果
# ============================
print("独立标签列表:", mlb.classes_)
print("one-hot 编码结果:\n", y_encoded)
