"""
元组的使用坑集
当元组只有一个元素时，一定要加逗号哈～
"""

animals = ["Cat", "Dog", "Fish"]
def add_snake(snake_type):
    animals.extend(snake_type)
    print(animals)

# 括号( )既可以表示tuple，又可以表示数学公式中的小括号
# 如果不用逗号明确表示()表示一个元组，则按小括号进行计算，数据类型为传入元素的类型
print("=====tuple only with simple item=======")
item = ("Python")
print(f"type = {type(item)}")
# 当类型为字符串时，遍历(item)将视为迭代遍历字符串
for i in item:
    print(i)
add_snake(item)
print("-"*20)

# 当元组只有一个元素时，一定要加入逗号
print("=====tuple with comma=======")
item = ("Python",)
print(f"type = {type(item)}")
for i in item:
    print(i)
add_snake(item)