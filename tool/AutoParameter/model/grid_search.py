"""
GridSearch网格搜索

"""

from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV

# 加载数据
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

# 定义网格参数
param_grid = {"C": [0.1, 1, 10, 100],
              "gamma": [0.01, 0.1, 1]}

# 利用网格参数和所需模型estimator，实例化GridSearch对象
grid_search = GridSearchCV(SVC(), param_grid, cv=5)

# 调用fit
# 拟合GridSearchCV对象不仅会搜索最佳参数，还会利用得到最佳交叉验证性能的参数在整个训练数据集上自动拟合一个新模型
grid_search.fit(X_train, y_train)
print("====best params===")
print(grid_search.best_params_)
print("===pred score===")
pred_score = grid_search.score(X_test, y_test)
print(pred_score)
