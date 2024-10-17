from PIL import Image


def images_to_pdf(image_list, output_pdf_path):
    # 打开第一个图片，作为PDF的基础
    images = [Image.open(img).convert('RGB') for img in image_list]

    # 保存所有图片为PDF，保存第一张作为基础，其他作为追加的页面
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])


# 示例图片列表
# image_files = ['data/1.jpg', 'data/2.jpg']  # 替换为你的图片路径
# output_pdf = 'file1.pdf'

image_files = ['data/3.jpg', 'data/4.jpg', 'data/5.jpg']  # 替换为你的图片路径
output_pdf = 'file2.pdf'

# 将图片合并为PDF
images_to_pdf(image_files, output_pdf)

print(f"PDF文件保存为: {output_pdf}")