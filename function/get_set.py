"""
Getter and setter usage.
"""

class Account:
    income_ratio = 0.8
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def run(self):
        print(f"Account user is {self.name}")

    @property
    def balance(self):
        # 定义balance的get()方法，使用@property装饰器进行修饰，方法名就是属性名
        return self.__balance

    @balance.setter
    def balance(self, balance):
        # 定义balance的set()方法，使用@balance.setter装饰器进行修饰，balance是属性名
        self.__balance = balance


account = Account("Anne", 100)
print(f"name = {account.name}")
print(f"balance = {account.balance}")
print(f"income_ratio = {account.income_ratio}")
print(f"income_ratio = {Account.income_ratio}")