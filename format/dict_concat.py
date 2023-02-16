"""
字典合并
"""
from functools import reduce

user_data = {"ID": "3312", "name": "Kylin", "degree": "junior"}
student_data = {"ID": "3312", "score": 78, "degree": "senior"}

dict_list = [user_data, student_data]

# 合并方式一，右边的字段会覆盖左边的同名键
concat_dict1 = {**user_data, **student_data}
print(concat_dict1)

# 合并方式2，python v3.9支持
# 否则会报错，TypeError: unsupported operand type(s) for |: 'dict' and 'dict'
print(user_data | student_data)
user_data |= student_data
print(user_data)

# 合并方式3，利用reduce
merged_dict = reduce(lambda x, y: {**x, **y}, dict_list)
print(merged_dict)
