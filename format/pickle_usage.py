from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import  pickle
import numpy as np
"""
自定义序列化
"""

X, y = load_iris(as_frame=True, return_X_y=True)

# 一般的预处理方法，都实现了pickle要求的相关方法，因此做无需特殊处理。
# 标准化训练集
scaler = StandardScaler()
scaler.fit(X)
X_scalered = scaler.transform(X)

# 序列化
# 序列化保存
with open('scaler.pkl', 'wb') as file:
    pickle.dump(scaler, file)

# 从文件中加载数据并进行反序列化
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
X_scalered_new = scaler.transform(X)
print(np.sum(X_scalered == X_scalered_new))

# 如果想要pickle自定义的方法，则需要实现__getstate__和__setstate__方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def running(self):
        print(f"{self.name} is running under downpour, whose age is {self.age}")

    def __getstate__(self):
        # 在序列化时，返回一个字典，不包含年龄信息
        return {'name': self.name}

    def __setstate__(self, state):
        # 在反序列化时，根据字典恢复对象状态
        self.name = state['name']
        # 这里我们不恢复age信息，以达到不保存年龄的目的
        self.age = None


person = Person(name="kylin", age=10)

# 将对象序列化并保存到文件
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)
# 从文件中加载数据并进行反序列化
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)

loaded_person.running()
