# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
多线程udp聊天室
"""
import socket
import threading


def receiveMsg(udp_socket):
    """
    接收数据并显示
    :return:
    """
    # 3. 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)[0].decode('utf-8')
        print(recv_data)


def sendMsg(udp_socket, dest):
    """
    发送数据
    :param udp_socket:
    :param dest:
    :return:
    """
    while True:
        send_data = input("输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), dest)


def main():
    """
    完成udp聊天器的整体控制
    :return:
    """
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("127.0.0.1", 7890))

    # 3. 输入目标ip和端口
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入端口："))
    dest = (dest_ip, dest_port)

    # 4. 创建线程执行功能
    t_recv = threading.Thread(target=receiveMsg, args=(udp_socket,))
    t_send = threading.Thread(target=sendMsg, args=(udp_socket, dest))

    # 5. 开启
    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()