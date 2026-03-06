import pandas as pd

def simple_demo(s, edges):
    bins_res = pd.cut(s, bins=edges)
    print(f"type bins_res: {type(bins_res)}")
    print(f"dtype bins_res: {bins_res.dtype}")

    df = pd.DataFrame({
        "value": s,
        "bin": bins_res
    })

    print(df)



def contain_lowest(s, edges):
    bins_res = pd.cut(
        s,
        bins=edges,
        include_lowest=True
    )

    df = pd.DataFrame({
        "value": s,
        "bin": bins_res
    })

    print(df)


def set_right_False(s, edges):
    bins_res = pd.cut(
        s,
        bins=edges,
        right=False
    )

    df = pd.DataFrame({
        "value": s,
        "bin": bins_res
    })

    print(df)


def equal_width_binning(s, bins_num):
    bins_res = pd.cut(s, bins=bins_num)

    df = pd.DataFrame({
        "value": s,
        "bin": bins_res
    })

    print(df)

def main():
    print("=====原始方式区间左开右闭=======")
    s = pd.Series([8, 12, 18, 25, 30, 31, 37, 44, 50, 52])
    edges = [10, 30, 50]
    simple_demo(s, edges)

    print("=====include_lowest=======")
    s = pd.Series([8, 10, 18, 20, 25, 30])
    edges = [10, 20, 30]
    contain_lowest(s, edges)

    print("=====right as False=======")
    s = pd.Series([8, 10, 18, 20, 25, 30])
    edges = [10, 20, 30]
    set_right_False(s, edges)

    print("=====设置分箱数进行等距分箱=====")
    s = pd.Series([10, 20, 30, 40, 50])
    bins_num = 10
    equal_width_binning(s, bins_num)


if __name__ == "__main__":
    main()