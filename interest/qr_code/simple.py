import qrcode
from MyQR import myqr
import numpy as np

"""
有两种生成qrcode的方式，例如qrcode和MyQR
"""


def qrcode_generate(info, save_path):
    img = qrcode.make(info)
    img.save(save_path)


def myqr_generate(info, save_path, insert_path=None):
    myqr.run(words=info, picture=insert_path, colorized=True, save_name=save_path)


def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str =''
    base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length =len(base_str) - 1

    for i in range(randomlength):
        random_str += base_str[np.random.randint(0, length)]

    return random_str


def main():
    info = generate_random_str()
    bg_path = "img/rabbit_bg.jpg"

    # generate by qrcode
    save_path_qrcode = "img/random_qrcode.png"
    qrcode_generate(info, save_path_qrcode)

    # generate by myqr
    save_path_myqr = "img/random_myqr2.png"
    myqr_generate(info, save_path_myqr, insert_path=bg_path)

main()
