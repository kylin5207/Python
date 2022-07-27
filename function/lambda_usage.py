"""
匿名函数与map
匿名函数的适用场景：在无需多处调用的场合使用，用户不关心函数的名字，只关心这种映射的关系。

"""

# 有一些函数的定义具有清晰简单的映射关系
# 但其实违背了“匿名”的含义，事实上它往往在无需多处调用的场合进行使用
simple_func = lambda x: 2*x
print(simple_func(2))

multi_func = lambda a, b : a + b
print(multi_func(1,2))

# 用户不关心函数的名字，只关心这种映射的关系
test_list = [(lambda x: x**2+1)(i) for i in range(7)]
print(test_list)

# Python 中提供了 map 函数来完成
# 但是它返回的是一个 map 对象，需要通过 list 转为列表
test_list2 = list(map(lambda x: x**2 + 1, range(7)))
print(test_list2)

# 对于多个输入值的函数映射，可以通过追加迭代对象实现
complex_list = list(map(lambda x, y: str(x)+'_'+y, range(5), list('abcde')))
print(complex_list)