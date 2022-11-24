"""
bisect 搜索
bisect(haystack,needle)在haystack（干草垛）里搜索 needle（针）的位置，该位置满足的条件是:把 needle 插入这个位置之后， haystack 还能保持升序。
也就是在说这个函数返回的位置前面的值，都小于或等于 needle 的值。
"""
import bisect

a = [0, 1, 5, 7, 19, 25]
a1 = bisect.bisect(a, 6)

# 这里返回的位置是3是因为：
# 为了保证插入这个数，还能保持列表升序，这个位置显而易见就在值5后面
print(a1)

# bisect函数其实是bisect_right函数的别名，后者还有个姊妹函数叫bisect_left。
# bisect_left函数是新元素会被放置于它相等的元素的前面，而 bisect_right返回的则是跟它相等的元素之后的位置。
# 这个返回3，是因为bisect会把新的元素放在相等元素后面即 2 + 1 = 3
a1 = bisect.bisect(a, 5)

# 这个返回2，是因为bisect_left会把新的元素放在相等元素前面即原来值5的索引位置2
a2 = bisect.bisect_left(a, 5)

print(a1, a2) # 3, 2


