"""
字典求和合并，相同键的values相加
字典排序，将字典按照键值大小进行排序
"""
import collections, functools, operator

dict_1 = {"A": 10, "B": 0, "C": 20}
dict_2 = {"A": 2, "C":10}

# 字典求和合并
counter = collections.Counter()
counter.update(dict_1)
counter.update(dict_2)
sum_dict = dict(counter)
print("====== sum concat ======")
print(sum_dict)

# 字典排序
sort_value_dict = sorted(sum_dict.items(), key=lambda x:x[1], reverse=True)
print("===== sorted by value ====")
print(sort_value_dict)






