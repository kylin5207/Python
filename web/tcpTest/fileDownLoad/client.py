# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
import socket
import time


def main():
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器ip port
    dest_ip = input("请输入下载服务器的ip：")
    dest_port = int(input("请输入下载服务器的端口号："))

    # 3. 连接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 4. 获取下载的文件名
    download_file_name = input("请输入要下载的文件名：")

    # 5. 将文件名发送服务器
    tcp_socket.send(download_file_name.encode("utf-8"))

    # 6. 接收文件中的数据
    recv_data = tcp_socket.recv(1024*1024)

    if recv_data:
        # 7. 保存接收到的数据
        # 为了避免重复，这里加入时间戳
        str_time = str(round(time.time() * 1000))
        with open(str_time + download_file_name, "wb") as f:
            f.write(recv_data)
    else:
        print("没有查找到相关文件，下载失败～")

    # 8. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()