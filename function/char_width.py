"""
全角和半角字符宽度问题处理
"""

s = "学号：0000006111"

# for ch in s:
#     if '\u4e00' <= ch <= '\u9fff':
#         print(ch)


# coding:utf-8
def all_to_half(all_string):
    """全角转半角"""
    full_char_list = list()
    full_index_list = list()
    half_string = ""
    for i, char in enumerate(all_string):
        inside_code = ord(char)
        if inside_code == 12288:  # 全角空格
            full_char_list.append(char)
            full_index_list.append(i)
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）
            full_char_list.append(char)
            full_index_list.append(i)
        elif '\u4e00' <= char <= '\u9fff':  # 中文字符
            full_char_list.append(char)
            full_index_list.append(i)

    print(f"中文及全角符号：{full_char_list}")
    print(f"中文及全角符号索引：{full_index_list}")

print(f"原字符串：{s}")
all_to_half(s)
