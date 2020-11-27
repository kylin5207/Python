# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
文件复制
（图片文件）
"""
with open("tm.jpg", "rb") as file:
    with open("copy.jpg", "wb") as copyFile:
        copyFile.write(file.read())
