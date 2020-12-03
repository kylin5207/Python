# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS

import socket
import time


def send_file(new_socket, client_addr):
    # 发送数据
    # 1。 获取用户要的文件名
    file_name = new_socket.recv(1024)
    print("客户端(%s)需要下载的文件是: %s" % (str(client_addr), file_name.decode("utf-8")))

    file_content = None

    # 2。打开文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件：%s" % file_name)

    # 3。 发送文件数据给客户端
    if file_content:
        new_socket.send(file_content)


def main():
    # 1. socket创建服务器端套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定ip和端口
    addr = ("127.0.0.1", 8899)
    tcp_server.bind(addr)

    # 3. 设置监听状态
    tcp_server.listen(128)

    while True:
        # 为多个客户端服务
        print("等待一个新的客户端～")

        # 4. 等待客户端连接
        new_socket, client_addr = tcp_server.accept()
        print("----新的客户已到达----")
        print("客户端地址：%s" % str(client_addr))

        # 5. 发送文件
        send_file(new_socket, client_addr)

        print("服务完毕")
        print("=" * 15)

        new_socket.close()

    # 6. 服务器关闭
    tcp_server.close()


if __name__ == "__main__":
    main()