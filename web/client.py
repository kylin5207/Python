# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
服务器端使用java实现了基于udp协议端socket
"""
import socket


class ClientSocket(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):

        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        IP = (self.ip, self.port)
        self.udp_socket.bind(IP)
        print("客户端socket已创建～")

    def send(self, data, destIp, destPort):
        # 目标地址的ip和端口
        destIp = (destIp, destPort)
        # 使用套接字收发数据
        self.udp_socket.sendto(data.encode('utf-8'), destIp)
        print("发送消息～")

    def recieve(self):
        # 获取服务器端信息,是个元组哦（收到的数据，(发送方ip，端口)）
        # 需要转码
        recv_data = self.udp_socket.recvfrom(1024)[0].decode('utf-8')

        print("来自服务器的消息：")
        print(recv_data)

    def close(self):
        # 关闭套接字
        self.udp_socket.close()


if __name__ == "__main__":
    client = ClientSocket("127.0.0.1", 7788)
    client.start()
    destIp = "127.0.0.1"
    destPort = 8888
    data = "hahah"
    client.send(data, destIp, destPort)
    client.close()