# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import socket

def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定一个本地信息
    IP = ("", 7788)
    udp_socket.bind(IP)
    print("客户端socket已创建～")

    while True:
        # 3. 发送数据
        data = input("输入请求信息：")
        # 目标地址的ip和端口
        destIp = ("", 8888)
        # 使用套接字收发数据
        udp_socket.sendto(data.encode('utf-8'), destIp)
        print("发送消息～")

        # 4. 接收数据，返回值是一个元组（接收的数据，（发送方ip，端口））
        receive = udp_socket.recvfrom(1024)

        # 5. 打印接收到的数据
        receive_data = receive[0].decode('utf-8')
        receive_address = receive[1]
        print(receive_data)
        print(receive_address)

    # 6. 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()