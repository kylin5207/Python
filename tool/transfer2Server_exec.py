import os
import paramiko
"""
服务器文件上传工具
"""


def transfile(localdir, remotepath, server):
    """
    远程传输函数
    :param localdir: 本地待上传目录
    :param remotepath: 目标目录
    :param server: 服务器地址
    :return:
    """
    # 设定用户名、密码
    username = "root"
    password = "Password"
    # 建立SSH连接
    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server, username=username, password=password)
    sftp = ssh.open_sftp()
    # 建立服务器目标目录
    remotedir = os.path.join(remotepath, "max_var")
    try:
        sftp.mkdir(remotedir)
    except:
        pass
    parent = os.walk(localdir)
    for walker in parent:
        pass
    for file in walker[2]:
        sftp.put(os.path.join(walker[0], file), os.path.join(remotedir, file))
    # 关闭链接
    ssh.close()
    print(localdir + " done")


# 待上传的文件名
file_name = "./data"

# 服务器ip和数据目录
server_ip_dir = ["192.0.0.1", "/data/"]

transfile(file_name, server_ip_dir[1], server_ip_dir[0])