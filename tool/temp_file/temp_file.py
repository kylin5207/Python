"""
Tempfile学习

Python的tempfile模块是用来创建临时文件或者文件夹的跨平台工具。
"""

import tempfile

# TemporaryFile返回一个类文件对象用作临时存储区, 它一关闭就会被销毁。
# 参数说明：
# `mode`参数：默认为`w+r`，以便文件在被创建时可以执行读写操作。
# `buffering`、`encoding`、`errors`和`newline`参数：用于解释`open()`函数行为。
# `dir`、`prefix`和`suffix`参数：与`mkstemp()`具有相同的含义和默认设置。
fp = tempfile.TemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, errors=None)

fp.write(b'Hello, Kylin')

# 读取数据
fp.seek(0)
print(fp.read())

# 上下文方式
# 完成上下文管理或销毁文件对象后，临时文件将从文件系统中删除。
with tempfile.TemporaryFile() as fp:
	fp.write(b'Hello Xiaoliang!')
	fp.seek(0)
	fp.read()


# 底层临时文件创建
# 多了delete参数
fp_2 = tempfile.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True)

# 高级临时目录创建函数
dp = tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)

# 底层临时文件创建函数mkstemp()
# mkstemp()函数以尽可能安全的方式创建临时文件，与TemporaryFile()函数不同，用户需要负责临时文件的删除。
tmp_file = tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)
print(tmp_file)
# 释放资源
import os
try:
    os.remove(tmp_file[1])
except OSError:
    pass