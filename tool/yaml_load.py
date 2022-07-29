"""
接口参数自动化
"""

import yaml
import os

class ReadYaml:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config"),
                                          "parameter.yaml")
        else:
            self.file_path = file_path
        self.data = self.read()

    def read(self):
        with open(self.file_path, 'r', encoding="utf-8") as f:
            # 使用yaml.load()加载yaml文件
            content = yaml.load(f, Loader=yaml.FullLoader)
            return content

    def get_value(self, param, config):
        return self.data[param][config]


if __name__ == "__main__":
    ry = ReadYaml()
    content = ry.data
    print(content)
    value = ry.get_value("user_space_size", "min")
    print(value)
