"""
list对象append和extend方法对比
- append()用于在列表末尾添加新的对象，输入参数为对象
- extend()用于在列表末尾追加另一个序列中的多个值，输入对象为元素队列
append是将输入对象添加到列表末尾；而extend则是将输入对象的可迭代对象添加到列表末尾。
"""

a = [(1,2), [9, 0, 8], {"name":"kylin", "age":23}]
print("======initial list=======")
print(a)
# 原始列表长度为3
print(f"Initial length equals {len(a)}")

print("*****Simple usage********")

# append方法
# append()是向列表尾部追加一个新元素，追加的元素仅占该列表的一个索引位
b = list()
b.append(a)
print("append output")
print(b)
print(f"After append, the list length equals {len(b)}")
print("-"*10)

# extend方法
# extend()向列表尾部追加一个可迭代对象(列表)，将可迭代对象中的每个元素都追加进来，并在该列表原有的基础上增加
c = list()
c.extend(a)
print("extend output")
print(c)
print(f"After extend, the list length equals {len(c)}")
print("-"*10)

# 更复杂的对比
print("********Embed usage********")
d = list()
# 遍历原列表中的每一个元素，将其使用append()追加
for n in a:
    d.append(n)
print(d)
print(f"After append, the list length equals {len(d)}")
print("-"*10)

e = list()
# 遍历原列表中的每一个元素，将其使用extend()追加
for n in a:
    e.extend(n)
print(e)
print(f"After extend, the list length equals {len(e)}")
print("-"*10)

# +与extend()在效果上具有相同的功能，但是实际上生成了一个新的列表来存放这两个列表的集合，只能用在两个列表相加上
m = [1, 2, 3]
n = [5, 6, 7]
plus = m + n
print(f"m id = {id(m)}")
print(f"n id = {id(n)}")
print(plus)
# 可以看到实际上生成了一个新的列表来存放这两个列表的集合
print(f"+ id = {id(plus)}")
