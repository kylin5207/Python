from typing import Union, Tuple
from reportlab.lib import units
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('msyh', r'./msyh.ttc'))

'''
用于生成包含content文字内容的水印pdf文件

content: 水印文本内容
filename: 导出的水印文件名
width: 画布宽度，单位：mm
height: 画布高度，单位：mm
font: 对应注册的字体代号
fontsize: 字号大小
angle: 旋转角度
text_stroke_color_rgb: 文字轮廓rgb色
text_fill_color_rgb: 文字填充rgb色
text_fill_alpha: 文字透明度


'''


def create_wartmark(content: str,
                    filename: str,
                    width: Union[int, float],
                    height: Union[int, float],
                    font: str,
                    fontsize: int,
                    angle: Union[int, float] = 45,
                    text_stroke_color_rgb: Tuple[int, int, int] = (0, 0, 0),
                    text_fill_color_rgb: Tuple[int, int, int] = (0, 0, 0),
                    text_fill_alpha: Union[int, float] = 1) -> None:
    # 创建PDF文件，指定文件名及尺寸，以像素为单位
    c = canvas.Canvas(f'{filename}.pdf', pagesize=(width * units.mm, height * units.mm))

    # 画布平移保证文字完整性
    # c.translate(0.1 * width * units.mm, 0.1 * height * units.mm)
    c.translate(0.5 * width * units.mm, 0.5 * height * units.mm)

    # 设置旋转角度
    c.rotate(angle)

    # 设置字体大小
    c.setFont(font, fontsize)

    # 设置字体轮廓彩色
    c.setStrokeColorRGB(*text_stroke_color_rgb)

    # 设置填充色
    c.setFillColorRGB(*text_fill_color_rgb)

    # 设置字体透明度
    c.setFillAlpha(text_fill_alpha)

    # 绘制字体内容
    c.drawString(0, 0, content)

    # 保存文件

    c.save()


create_wartmark(content='kylin',
                filename='watermask',
                width=400,
                height=400,
                font='msyh',
                fontsize=60,
                text_fill_alpha=0.2)