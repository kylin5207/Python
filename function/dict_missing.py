"""
通过定义字典内置的__missing__()函数，实现斐波那契
"""
class FibDict(dict):
    def __init__(self):
        self[0] = self[1] = 1

    def __missing__(self, k):
        """
        按照Python的约定就知道它是一个magic method，有点像defaultdict。
        当 dict 查找 key 失败(missing)的时候，会由Python解释器自行调用。
        换句话说，如果试图从dict中获取不存在的key，就会执行这个方法，我们可以在这个方法中做一些补救措施，
        避免抛出默认的 KeyError 异常。
        """
        fibk = self[k] = self[k-1] + self[k-2]
        return fibk

fibd = FibDict()
print(fibd[10])