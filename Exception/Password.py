# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
主动抛出异常：
  raise的使用
  密码长度检测
"""


def input_password(password):

    if len(password) < 8:
        raise  Exception("密码长度不够")
    else:
        return password


if __name__ == "__main__":
    password = input("输入密码：")
    try:
        input_password(password)
    except Exception as result:
        print("登陆失败, 原因：%s" % result)
    else:
        print("登陆成功")
    finally:
        print("~")