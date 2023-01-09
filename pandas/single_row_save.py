import pandas as pd
import os

dir = "dataset"
if not os.path.exists(dir):
	os.mkdir(dir)

def process_data():
	data = pd.read_excel("测试数据集.xlsx", header=0)
	n_row = data.shape[0]
	type_dict = dict(zip(data.columns, data.dtypes.values))

	for i in range(n_row):
		row = data.iloc[i]
		path_name = int(row["Agent"])
		df = pd.DataFrame(row).T
		df = df.astype(type_dict)
		df.to_csv(f"dataset/{path_name}.csv", index=False)

process_data()
