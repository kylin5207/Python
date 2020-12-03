# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
使用套接字socket包创建UDP套接字

    socket.socket(param1，param2)：
        参数1：指定协议
        参数2：指定套接字类型

"""
import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("----run-----")

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()