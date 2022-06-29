"""
获取文件夹下的图片路径
"""
import os

def getAllImage(folderPath, imageList):
    extend_name = ["jpg", "jpeg", "png", "bmp"]
    for item in os.listdir(folderPath):
        if os.path.isdir(os.path.join(folderPath, item)):
            subFolderPath = os.path.join(folderPath, item)
            getAllImage(subFolderPath, imageList)
        else:
            filePath = os.path.join(folderPath, item)
            if os.path.isfile(filePath):
                if item.split('.')[-1] in extend_name:
                    imageList.append(filePath)
    return imageList

def load_pic(path):
    imageList = []
    getAllImage(path, imageList)
    print("len(imageList): ", len(imageList))
    return imageList

if __name__ == "__main__":
    path = r"./vector_distance/data/base_img"
    pic_list = load_pic(path)
    print(pic_list)