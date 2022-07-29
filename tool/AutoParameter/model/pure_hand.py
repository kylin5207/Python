"""
纯手动暴力搜索的方式
"""
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. 加载数据
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

# 手动暴力
best_score = 0
for gamma in [0.01, 0.1, 1]:
    for c in [0.1, 1, 10, 100]:
        svm = SVC(C=c, gamma=gamma)
        svm.fit(X_train, y_train)
        score = svm.score(X_test, y_test)

        if score > best_score:
            best_score = score
            best_parameters = {"C":c, "gamma":gamma}

print(f"best parameters = {best_parameters}")
print(f"best score = {best_score}")

