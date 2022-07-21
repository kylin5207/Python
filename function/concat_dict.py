"""
字典合并，若存在相同的键，则合并～

"""
def concat_dicts(dict_a, dict_b):
    temp = dict()
    for key in dict_a.keys() | dict_b.keys():
        temp[key] = sum([d.get(key, 0) for d in (dict_a, dict_b)])

    return temp


if __name__ == "__main__":
    dict_a = {"a": 2, "b": 4, "d": 7}
    dict_b = {"a": 3, "b": 5, "e": 8}
    print(concat_dicts(dict_a, dict_b))