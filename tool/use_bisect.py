# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
python内置二分模块bisect
用于有序序列的插入和查找
·查找：bisect(array, item)
·插入: insort(array, item)
"""
import bisect

a = [1, 4, 7, 10, 12]
b = [1, 4, 7, 10, 12]
# bisect用于查找元素要插入的位置
position = bisect.bisect(a, 13)
print(position)

# 用list的insert插入
a.insert(position, 13)
print(f'a = {a}')

# 用bisect的insort插入
bisect.insort(b, 13)
print(f'b = {b}')

# bisect还有bisect_left
# 当插入的元素和序列中的某一个元素相同时，插入到该元素的前面（左边，left），还是后面（右边）；
# 如果是查找，则返回该元素的位置还是该元素之后的位置。

