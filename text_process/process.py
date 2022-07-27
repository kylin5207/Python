"""
文本处理的五类操作：拆分、合并、匹配、替换、提取
"""
import pandas as pd

# 一、拆分
# str.split()能够把字符串的列进行拆分，其中:
# 第一个参数为正则表达式，
# 可选参数包括从左到右的最大拆分次数n，是否展开为多个列 expand 。
s = pd.Series(['上海市黄浦区方浜中路249号', '上海市宝山区密山路5号'])
print(s.str.split('[市区路]'))

# 最大拆分2次，展开为多个列
print(s.str.split('[市区路]', n=2, expand=True))

# =======================
# 二、合并
# 关于合并一共有两个函数，分别是 str.join 和 str.cat 。
# str.join 表示用某个连接符把 Series 中的字符串列表连接起来，如果列表中出现了非字符串元素则返回缺失值：
s = pd.Series([['a','b'], [1, 'a'], [['a', 'b'], 'c']])
print(s.str.join('-'))

# str.cat 用于合并两个序列，主要参数为连接符sep 、连接形式join以及缺失值替代符号na_rep ，其中连接形式默认为以索引为键的左连接。
s1 = pd.Series(['a','b'])
s2 = pd.Series(['cat','dog'])
# sep指定连接符，默认使用左连接
print(s1.str.cat(s2, sep='-'))

s2.index = [1, 2]
print(s1.str.cat(s2, sep='-', na_rep='?', join='outer'))

# =======================
# 三、匹配
# str.contains 返回了每个字符串是否包含正则模式的布尔序列
s = pd.Series(['my cat', 'he is fat', 'railway station'])
print(s.str.contains('\s\wat'))
# 在 str.contains 的正则中使用 ^ 和 $ 来实现正则匹配：
print(s.str.contains('^[m|h]'))

# str.startswith 和 str.endswith 返回了每个字符串以给定模式为开始和结束的布尔序列，
# 它们都不支持正则表达式
print(s.str.startswith('my'))
print(s.str.endswith('t'))
# 如果需要用正则表达式来检测开始或结束字符串的模式，可以使用 str.match ，
# 其返回了每个字符串起始处是否符合给定正则模式的布尔序列
print(s.str.match('m|h'))

# 除了上述返回值为布尔的匹配之外，还有一种返回索引的匹配函数
# str.find 返回从左到右第一次匹配的位置的索引，未找到则返回-1
# str.rfind 返回从右到左第一次匹配的位置的索引，未找到则返回-1。
# 需要注意的是这两个函数不支持正则匹配，只能用于字符子串的匹配
s = pd.Series(['This is an apple. That is not an apple.'])
print(s.str.find('apple'))
print(s.str.rfind('apple'))

# =======================
# 四、替换
# str.replace 和 replace 并不是一个函数，在使用字符串替换时应当使用前者。
s = pd.Series(['a_1_b','c_?'])
print(s.str.replace('\d|\?', 'new', regex=True))

# =======================
# 五、提取
# 提取既可以认为是一种返回具体元素（而不是布尔值或元素对应的索引位置）的匹配操作，也可以认为是一种特殊的拆分操作。
# 前面提到的 str.split 例子中会把分隔符去除，这并不是用户想要的效果，这时候就可以用 str.extract 进行提取：
s = pd.Series(['上海市黄浦区方浜中路249号', '上海市宝山区密山路5号'])
pat = '(\w+市)(\w+区)(\w+路)(\d+号)'
print(s.str.extract(pat))
# 通过子组的命名，可以直接对新生成 DataFrame 的列命名：
pat = '(?P<市名>\w+市)(?P<区名>\w+区)(?P<路名>\w+路)(?P<编号>\d+号)'
print(s.str.extract(pat))
# str.extractall 不同于 str.extract 只匹配一次，它会把所有符合条件的模式全部匹配出来，如果存在多个结果，则以多级索引的方式存储：
s = pd.Series(['A135T15,A26S5','B674S2,B25T6'], index = ['my_A','my_B'])
pat = '[A|B](\d+)[T|S](\d+)'
print(s.str.extractall(pat))
