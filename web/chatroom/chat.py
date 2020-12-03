# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import socket


def send_msg(udp_socket):
    """
    发送消息
    :return:
    """
    # 首先获取目标ip和端口
    dest_ip = input("请输入目标ip：")
    dest_port = int(input("请输入端口号："))
    destIP = (dest_ip, dest_port)

    # 获取要发送的内容
    send_data = input("输入要发送的内容：")
    udp_socket.sendto(send_data.encode("utf-8"), destIP)
    print("发送成功")


def recv_msg(udp_socket):
    """
    接收数据
    :return:
    """
    receive_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (receive_data[1], receive_data[0].decode("utf-8")))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定端口信息
    udp_socket.bind(("", 7788))

    # 3. 循环处理问题
    while True:
        print("----Kylin聊天室------")
        print("1. 发送消息".center(20))
        print("2. 接收消息".center(20))
        print("3. 退出系统".center(20))
        op = input("请输入功能：")

        if op == "1":
            # 3.1 发送数据
            send_msg(udp_socket)

        # 如果收到来自服务器的信息，则会将信息保存在缓存中，这容易造成缓存的溢出
        elif op == "2":
            # 3.2 接收与显示问题
            recv_msg(udp_socket)

        elif op == "0":
            print("感谢您的使用，关闭聊天")
            break

        else:
            print("输入指令有误")


if __name__ == "__main__":
    main()