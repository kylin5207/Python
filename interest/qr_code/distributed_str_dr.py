import qrcode
from PIL import Image
import numpy as np

def qr_make(k, info, bg_img="img/rabbit_bg.jpg"):
    qr = qrcode.QRCode(version=5)

    # 向二维码中添加信息
    qr.add_data(info)

    qr.make(fit=True)

    # 创建二维码的图像并返回，默认为 PIL 图像。如果要让二维码有颜色，可以在这里设置fill_color, back_color
    img = qr.make_image()
    # 将二维码设置为彩色
    img = img.convert('RGBA')
    # 打开logo图片
    logo = Image.open(bg_img)
    # 二维码尺寸
    img_w, img_h = img.size
    # 默认logo最大为图片的1/4
    factor=4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    # logo size
    logo_w, logo_h = logo.size

    if logo_w > size_w or logo_h > size_h:
        logo_w = size_w
        logo_h = size_h

    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS).convert("RGBA")
    l_w = int((img_w - logo_w)/2)
    l_h = int((img_h - logo_h)/2)

    # 替换指定未知
    img.paste(logo, (l_w, l_h), logo)
    img.show()
    img.save(f"img/distributed/{k}.png")


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

def split_random(info, n):
    indexes = np.random.choice(len(info), n-1, replace=False).tolist()
    indexes.insert(0, 0)
    indexes.append(len(info))

    sub_info = []
    for i in range(n):
        sub_info.append(info[indexes[i]:indexes[i+1]])

    return sub_info


def main():
    n = 3
    # generate info
    info = generate_random_str(42)
    print(f"info = {info}")

    # distribute info
    sub_info = split_random(info, n)
    print(f"sub_info = {sub_info}")

    # make qr code
    for i in range(n):
        qr_make(i, sub_info[i], bg_img="img/rabbit_bg.jpg")

main()
