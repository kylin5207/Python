from typing import List
from pikepdf import Pdf, Page, Rectangle

'''
向目标pdf文件批量添加水印
target_pdf_path:目标pdf文件路径+文件名
watermark_pad_path:水印pdf文件路径+文件名
nrow:水印平铺的行数
ncol:水印平铺的列数
skip_pages:需要跳过不添加水印的页数

'''


def add_watemark(target_pdf_path: str,
                 watermark_pdf_path: str,
                 nrow: int,
                 ncol: int,
                 skip_pages: List[int] = []) -> None:
    # 选择需要添加水印的pdf文件
    target_pdf = Pdf.open(target_pdf_path)

    # 读取水印pdf文件并提取水印
    watermark_pdf = Pdf.open(watermark_pdf_path)
    watermark_page = watermark_pdf.pages[0]

    # 遍历目标pdf文件中的所有页，批量添加水印
    for idx, target_page in enumerate(target_pdf.pages):
        for x in range(ncol):
            for y in range(nrow):
                # 向目标页指定范围添加水印
                target_page.add_overlay(watermark_page,
                                        Rectangle(target_page.trimbox[2] * x / ncol,
                                                  target_page.trimbox[3] * y / nrow,
                                                  target_page.trimbox[2] * (x + 1) / ncol,
                                                  target_page.trimbox[3] * (y + 1) / nrow
                                                  ))
    # 保存PDF文件，同时对pdf文件进行重命名，从文件名第7位置写入后缀名
    target_pdf.save(target_pdf_path[:6] + '_已添加水印.pdf')


add_watemark(target_pdf_path='initial.pdf',
             # 把生成的水印示例，添加到目标水印文件中
             watermark_pdf_path='demo.pdf',
             nrow=2,
             ncol=3,
             skip_pages=[0])