"""
带有 if 选择的条件赋值，其形式为 value = a if condition
"""

voice = "miao"
value = "cat" if "miao".__eq__(voice) else "dog"
print(value)