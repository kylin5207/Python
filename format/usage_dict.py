# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
python创建字典的五种方式
"""

# 方式一：直接创建
dict1 = {"age": 1, "name": "Kylin", "sex": "boy"}
print(dict1)

# 方式二：using index
key = ["age", "name", "sex"]
value = [10, "Kylin", "boy"]
dict2 = {}
for i in range(len(key)):
    dict2[key[i]] = value[i]

print(dict2)

# 方式三：使用zip
dict3 = {}
for k, v in zip(key, value):
    dict3[k] = v
print(dict3)

# 方式四：zip加直接创建
dict4 = {k: v for k, v in zip(key, value)}
print(dict4)

# 方式五：利用构造方法传入zip创建
dict5 = dict(zip(key, value))
print(dict5)