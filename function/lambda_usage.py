"""
匿名函数lambda
- Python 使用 lambda 关键字来创建匿名函数。这种函数被称为“匿名”，因为它们没有显式的名称。
- 语法
    lambda arguments: expression
    - arguments: 参数列表，和普通函数的参数类似，可以有多个参数，用逗号分隔。
    - expression: 一个表达式，它基于给定的参数进行计算并返回结果。这个表达式只能有单一的逻辑，不能包括命令或多个表达式。
- 使用场景
    Lambda 函数在需要简单函数的地方非常有用，如排序操作、数据过滤等。
    由于它们的定义很短，经常直接嵌入到其他函数调用中，例如在列表处理函数（如 map(), filter(), sorted()）中。但是，如果逻辑变得复杂，建议使用标准的函数定义方式，以提高代码的可读性。
- 例如：计算折扣价格
    假设我们想根据产品的原价和季节来计算折扣后的价格。折扣规则如下：
    ·如果季节是“夏季”，则打 20% 的折扣。
    ·如果季节是“冬季”，则打 30% 的折扣。
    ·其他季节打 10% 的折扣。
"""

def compute_price(original_price, season):
    # 定义一个 lambda 函数来计算折扣价格
    calculate_discount = lambda price, season: price * 0.8 if season == '夏季' else (
                                                price * 0.7 if season == '冬季' else price * 0.9)
    # 计算折扣后价格
    discounted_price = calculate_discount(original_price, season)
    return discounted_price


def calculator(op):
    if op == "+":
        return lambda a, b: a + b
    elif op == "-":
        return lambda a, b: a - b
    elif op == "*":
        return lambda a, b: a * b
    elif op == "/":
        return lambda a, b: a / b
    else:
        raise ValueError(f"Invalid operator as {op}")


if __name__ == '__main__':
    print("====demo1: 计算器模拟===")
    a = 10
    b = 2
    func1 = calculator(op="-")
    print(f"a = {a}, b = {b}, {a} - {b} = {func1(a, b)}")
    func2 = calculator(op="*")
    print(f"a = {a}, b = {b}, {a} * {b} = {func2(a, b)}")

    print("=====demo2: 折扣价格计算=====")
    original_price = 100  # 原价
    season = '夏季'       # 当前季节
    discounted_price = compute_price(original_price, season)
    print(f'原价为 {original_price} 元，季节为 {season}，折扣后价格为 {discounted_price:.2f} 元')


