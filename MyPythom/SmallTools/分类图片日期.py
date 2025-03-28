# -*- coding = utf-8 -*-
# @Time:2024/11/12 16:44
# @Author:ck
# @File:分类图片日期
# @Software:PyCharm
import os
import shutil
from PIL import Image
from tqdm import tqdm
from datetime import datetime
def GetImageDateTime(image_path):
    try:
        image = Image.open(image_path)
        ExifData = image._getexif()
        if not ExifData:
            return None
        DateStrTime = ExifData.get(36867)
        if DateStrTime:
            DateStrTime = DateStrTime.split(" ")[0]
            return datetime.strptime(DateStrTime, "%Y:%m:%d").date()
    except Exception as e:
        print(f"无法读取图片日期: {image_path} - 错误: {e}")
    return None
def WortImages_ByDate(source_folder):
    unknown_folder = os.path.join(source_folder, "Unknown_Date")
    os.makedirs(unknown_folder, exist_ok=True)
    files = [f for f in os.listdir(source_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".heic", ".tiff"))]
    total_files = len(files)
    with tqdm(total=total_files, desc="分类图片", unit="file") as pbar:
        for filename in files:
            FilePath = os.path.join(source_folder, filename)
            image_date = GetImageDateTime(FilePath)
            if image_date:
                target_folder = os.path.join(source_folder, image_date.strftime("%Y-%m-%d"))
            else:
                target_folder = unknown_folder
            os.makedirs(target_folder, exist_ok=True)
            TargetPath = os.path.join(target_folder, filename)
            try:
                shutil.move(FilePath, TargetPath)
            except Exception as e:
                print(f"移动文件失败: {filename} - 错误: {e}")
            pbar.update(1)

if __name__ == "__main__":
    source_folder = input("请输入要整理的图片文件夹路径：")
    WortImages_ByDate(source_folder)
