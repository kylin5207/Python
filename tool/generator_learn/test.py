import numpy as np

class DataGenerator:
    def __init__(self, seed, left, right):
        self.seed = seed
        self.left = left
        self.right = right
        np.random.seed(seed)

    def generate(self, k):
        while True:
            print("***start**")
            yield np.random.randint(self.left, self.right, size=k)
            print("***end**")


data_selector = DataGenerator(0, 0, 10)
k = 10
print(next(data_selector.generate(k)))
print(next(data_selector.generate(k)))