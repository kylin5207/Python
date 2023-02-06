import qrcode
from PIL import Image

# version 控制二维码大小，取值为1时，大小为21*21。
# border 控制二维码四周留白的格子数，默认为4
# box_size 控制二维码中每个格子的像素数，默认为 10。
# image_factory 选择生成图片的形式，默认为 PIL 图像

qr = qrcode.QRCode(version=5)

# 向二维码中添加信息
qr.add_data("Hello, world")

# 当fit参数为真或者没有给出version参数时，将会调用best_fit方法来找到适合数据的最小尺寸。
# 如果没有设置mask_pattern，将会调用best_mask_pattern方法来找到找到最有效的掩模图案。
# 最后将这些数据传递给makeImpl方法来生成二维码。与qrcode本体的make方法不一样的是，这个方法没有任何返回值。

qr.make(fit=True)

# 创建二维码的图像并返回，默认为 PIL 图像。如果要让二维码有颜色，可以在这里设置fill_color, back_color
img = qr.make_image()
# 将二维码设置为彩色
img = img.convert('RGBA')
# 打开logo图片
logo = Image.open("img/rabbit_bg.jpg")
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
img.save("img/hello2.png")
