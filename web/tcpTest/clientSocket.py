# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
Tcp客户端端实现
"""
import socket


def main():
    # 1. 创建tcp套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 连接服务器
    address = ("127.0.0.1", 8888)
    tcp_client.connect(address)

    # 3. 发送/接收数据
    send_data = input("请输入数据：")
    tcp_client.send(send_data.encode("utf-8"))

    # 4. 关闭套接字
    tcp_client.close()


if __name__ == "__main__":
    main()
