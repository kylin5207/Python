# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
Tcp服务器端的实现
"""
import socket


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

        while True:
            # 只为一个客户端服务
            # 5. 接收/发送数据
            # 如果recive解阻塞，有两种方式：
            #   客户端发数据
            #   客户端调用close，关闭socket
            data = new_socket.recv(1024)

            # 如果接收的数据的⻓度为0， 则意味着客户端关闭了链接
            if not data:
                break

            print(data.decode("utf-8"))

            new_socket.send("connect successfully.".encode("utf-8"))

        print("服务完毕")
        print("=" * 15)

        new_socket.close()

    # 6. 服务器关闭
    tcp_server.close()


if __name__ == "__main__":
    main()