# -*- coding = utf-8 -*-
# @Time:2024/11/12 17:42
# @Author:ck
# @File:文件后缀名增加和删除
# @Software:PyCharm


import os

def add_suffix(filedir, suffix):
    for root, _, files in os.walk(filedir):
        for filename in files:
            FilePathAddSuffix = os.path.join(root, filename)
            base, ext = os.path.splitext(filename)
            if ext != suffix:
                new_name = f"{base}{ext}{suffix}"
                try:
                    os.rename(FilePathAddSuffix, os.path.join(root, new_name))
                    print(f"已添加后缀: {new_name}")
                except Exception as e:
                    print(f"重命名失败: {FilePathAddSuffix} - 错误: {e}")

def remove_suffix(filedir, suffix):
    for root, _, files in os.walk(filedir):
        for filename in files:
            FilePathRemovesuffix = os.path.join(root, filename)
            base, ext = os.path.splitext(filename)
            if ext == suffix:
                new_name = base
                try:
                    os.rename(FilePathRemovesuffix, os.path.join(root, new_name))
                    print(f"已删除后缀: {new_name}")
                except Exception as e:
                    print(f"重命名失败: {FilePathRemovesuffix} - 错误: {e}")

def main():
    FilePathMain = input("请输入文件夹路径：")
    suffix = input("请输入要添加或删除的后缀名（例如 .txt）：")
    if not FilePathMain or not suffix:
        print("文件路径和后缀名不能为空！")
        return
    print("请选择操作：")
    choice = input("请输入选择（增加/删除）：")
    if choice == "增加":
        add_suffix(FilePathMain, suffix)
    elif choice == "删除":
        remove_suffix(FilePathMain, suffix)
    else:
        print("无效选择，请重新运行程序并选择 ")

if __name__ == "__main__":
    main()
