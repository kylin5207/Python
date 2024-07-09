import json

data = {'hive': 1, 'hadoop': 2, 'hbase': 3, 'flink': 4, 'ambari': 5, "深度学习": 6}
print("data数据类型: ", type(data))

# 将一个Python数据类型列表进行json格式的编码
json_data = json.dumps(data, ensure_ascii=False)
print("json_data数据类型: ", type(json_data))
print(f"json_data context: json_data")

# 将json编码解码为python对象
data_obj = json.loads(json_data)
print(f"after loads type = {type(data_obj)}")

# 写入文件
with open('data.json', 'w') as file:
    json.dump(data, file)

# 读取文件并解码
with open('data.json', 'r') as file:
    data_obj2 = json.load(file)

print(f"reload type = {type(data_obj2)}, context = {data_obj2}")
