# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
完整的异常检测：
try:
   执行代码
except 错误类型1：
   相关处理
except 错误类型2：
   相关处理
except Exception as result:
   print("未知错误：%s" % result)
else:
   没有出现异常时执行的代码
finally:
   无论是否有异常，都会执行的代码
"""
try:
    num1 = int(input("输入被除数："))
    num2 = int(input("输入除数："))
    division = num1 / num2
    print(division)
except ValueError:
    print("输入参数类型错误")
except ZeroDivisionError:
    print("除数不为0哦")
except Exception as result:
    print("未知错误：%s" % result)
else:
    print("～")
finally:
    print("计算结束")
