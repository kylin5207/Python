"""
在密码学中，SHA-256 用于生成密码或其他敏感数据的哈希值，以安全地存储这些信息。
由于SHA-256 是单向函数，即从哈希值不能推导出原始数据，因此增加了安全性。
"""
import numpy as np
import hashlib

def generate_hashed_id(id_number):
    # 创建哈希对象，使用 SHA-256 算法生成的哈希值总是以256位的二进制形式存在
    hasher = hashlib.sha256()

    # id_number 字符串被编码为 UTF-8 格式的字节串，
    # 然后使用 update() 方法添加到之前创建的哈希对象中。
    # update() 方法可以被多次调用，以便分步骤地添加数据
    hasher.update(id_number.encode('utf-8'))

    # 完成所有数据的哈希计算并返回一个64字符长的十六进制字符串。
    # 这个字符串是哈希值的最终形式，表示为十六进制是为了便于阅读和存储。
    hashed_id = hasher.hexdigest()
    return hashed_id


id_number = np.arange(0, 10).astype("str")

hashed_id = [generate_hashed_id(i) for i in id_number]
print(hashed_id)