# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import hashlib

"""
MD5数据一致性
"""

if __name__ == "__main__":
    md5 = hashlib.md5()
    md5.update("This is a sentence".encode('utf-8'))
    md5.update("This is a second sentence".encode('utf-8'))
    print("乱码: ", md5.digest())
    print("MD5: ", md5.hexdigest())
    print(md5.digest_size, md5.block_size)