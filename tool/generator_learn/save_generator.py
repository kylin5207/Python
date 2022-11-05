import pickle

def generate(left, right):
    import random
    while True:
        print("***start**")
        yield random.randint(left, right)
        print("***end**")


g = generate(10, 16)
print(next(g, 19, 25))
print(next(g))
print(next(g))