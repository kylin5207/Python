"""
接口参数自动化
"""
import time
import numpy as np
import yaml
import os
from hyperopt import hp, fmin, rand
import numpy as np

class AutoSearch:
    def __init__(self, config_file=None):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        """
        加载配置文件
        :param config_file: str, 配置文件路径
        :return:
        """
        if config_file is None:
            config_file = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config"), "parameter.yaml")
        try:
            with open(config_file, 'r', encoding="utf-8") as f:
                # 使用yaml.load()加载yaml文件
                content = yaml.load(f, Loader=yaml.FullLoader)
        except FileNotFoundError:
            print("Config file has not been found.")
        return content

    def tune(self, algo=rand.suggest, max_evals=100):
        """
        自动选择参数
        :param algo: str, 搜索算法, default=rand.suggest
                    - hyperopt.rand.suggest, 随机搜索
                    - hyper opt.anneal.suggest, 模拟退火
                    - hyperopt.tpe.suggest, TPE算法
        :param max_evals: int, 最大执行次数, default=100
        :return: best, dict, 存放最佳参数字典
        """
        # 获取用于搜索的网格
        search_grid = self.get_search_grid()

        # 对参数进行全排列，枚举参数组合，返回最佳参数
        best = fmin(self.objective, search_grid, algo=algo, max_evals=100)

        return best

    def objective(self, args):
        """
        由于我们选择的是运行时间最短的参数，这里计时查看
        :param args: 用于搜索的参数
        :return:
        """
        x, y = args

        try:
            t1 = time.time()
            # 便于测试，内容随便写的
            for i in range(x):
                for j in range(y):
                    num = i + j
            t2 = time.time()
            run_time = t2 - t1

        except Exception:
            run_time = 1000000

        return run_time

    def get_search_grid(self):
        """
        获得用于搜索的网格
        :return: list, 搜索列表
        """
        search_list = list()
        for param in self.config.keys():
            # 根据设置的最值，生成对应参数的网格搜索值
            start = 1 if "min" not in self.config[param].keys() else self.config[param]['min']
            end = 10000 if "max" not in self.config[param].keys() else self.config[param]['max']
            select_param = hp.randint(param, start, end+1)
            search_list.append(select_param)

        return search_list


if __name__ == "__main__":
    # 初始化自动搜索类，可以输入存放待搜索参数的文件地址，否则使用默认文件
    auto = AutoSearch()
    # 调参，可以指定参数选择方法（默认随机），迭代次数（默认100）
    best = auto.tune()
    # 查看结果
    print(best)
