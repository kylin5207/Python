from hyperopt import hp, fmin, rand, tpe, space_eval

# 定义参数空间
space = [hp.uniform('x', 0, 1), hp.normal('y', 0, 1)]

# 定义用于最小化的函数
def objective(args):
    x, y = args
    return x**2 + y**2

# algo用于设定搜索的算法，rand.suggest()采用随机搜索
# fmin最小化目标函数：在搜索空间内进形线线搜索，去最小化目标函数（也可以最大化，见官方文档）
best = fmin(objective, space, algo=rand.suggest, max_evals=100)
print(best)
print(space_eval(space, best))

