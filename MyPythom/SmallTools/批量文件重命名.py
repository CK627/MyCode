# -*- coding = utf-8 -*-
# @Time:2024/11/26 20:20
# @Author:ck
# @File:批量文件重命名
# @Software:PyCharm
import os
import time


def rename_files(directory, log_file):
    if not os.path.exists(directory):
        print("指定目录不存在！")
        return
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != ".DS_Store"]
    files.sort()

    with open(log_file, 'w') as log:
        for idx, file in enumerate(files, start=1):
            old_path = os.path.join(directory, file)
            new_name = f"{idx}{os.path.splitext(file)[1]}"
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log.write(f"{timestamp} - {file} - {new_name}\n")
            print(f"已将 {file} 重命名为 {new_name}")
    print(f"所有文件重命名完成，日志已保存到 {log_file}")


def restore_files(directory, log_file):
    if not os.path.exists(log_file):
        print("日志文件不存在！无法恢复。")
        return

    with open(log_file, 'r') as log:
        lines = log.readlines()

    for line in lines:
        parts = line.strip().split(" - ")
        if len(parts) == 3:
            _, old_name, new_name = parts
            old_path = os.path.join(directory, old_name)
            new_path = os.path.join(directory, new_name)

            if os.path.exists(new_path):
                os.rename(new_path, old_path)
                print(f"已将 {new_name} 恢复为 {old_name}")
            else:
                print(f"文件 {new_name} 不存在，跳过。")
    print("文件名恢复完成。")

def main():
    print("请选择功能：")
    print("1: 批量更改文件名")
    print("2: 根据日志恢复文件名")
    choice = input("请输入选项（1或2）：")
    directory = input("请输入目标目录路径：")
    log_file = os.path.join(directory, "rename_log.txt")

    if choice == "1":
        rename_files(directory, log_file)
    elif choice == "2":
        restore_files(directory, log_file)
    else:
        print("无效选项！")

if __name__ == "__main__":
    main()
