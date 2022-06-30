"""
ModuleNotFoundError: 调用其他python代码中实现的类，出现加载模型error
原因：当前路径下木有调用python代码的路径
解决：手动添加路径至sys.path
"""
import os, sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.insert(0, os.path.abspath(os.path.join(__dir__, '..')))

from check_module import Student


if __name__ == "__main__":
    student = Student("kylin", 18)
    print(student)