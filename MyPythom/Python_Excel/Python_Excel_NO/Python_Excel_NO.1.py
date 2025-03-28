# -*- coding = utf-8 -*-
# @Time:2023/10/19 11:48
# @Author:CK
# @File:Python_Excel_NO.1
# @Software:PyCharm
import os
from tkinter import Tk, filedialog
import PySimpleGUI as sg
import pandas as pd

def Python_Excel_Data_Processing(file_path, folder_name):
    if not file_path:
        sg.popup_error("请选择一个Excel文件")
        return

    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        unique_categories = df["人员名称"].unique()
        original_file_directory = os.path.dirname(file_path)
        output_folder = os.path.join(original_file_directory, folder_name)
        os.makedirs(output_folder, exist_ok=True)

        for category in unique_categories:
            category_df = df[df["人员名称"] == category]
            row_count = len(category_df)
            output_file = os.path.join(output_folder, f'{category} 共打卡{row_count}次.xlsx')
            category_df.to_excel(output_file, index=False, engine='openpyxl')

        # Create a summary Excel file
        summary_data = [(category, len(df[df["人员名称"] == category])) for category in unique_categories]
        summary_df = pd.DataFrame(summary_data, columns=["导师", "打卡次数"])
        summary_file_path = os.path.join(output_folder, '各学院打卡次数统计.xlsx')
        summary_df.to_excel(summary_file_path, index=False, engine='openpyxl')

        sg.popup("处理完成！", title="成功")
    except Exception as e:
        sg.popup_error(f"处理时出错: {str(e)}", title="错误")

layout = [[sg.Text("Excel表格数据处理", grab=True)], [sg.Text("使用说明：\n鼠标悬浮在输入框有提示")],
    [sg.Text("选择Excel文件", enable_events=True, tooltip=f'输入或者点击“选择Excel文件”获取文件路径', size=(15, 1)),
     sg.Input(key='file_path', tooltip=f'示例：C:/Users/Administrator/Desktop/1.xlsx')],
    [sg.Text("新建文件夹名称", enable_events=True, tooltip=f'输入需要新建存放文件夹的名称，默认路径是源Excel表格路径', size=(15, 1)),
     sg.Input(key='folder_name', tooltip=f'示例：整理')],
    [sg.Button("开始"), sg.Button("退出")], ]

sg.theme("LightBlue2")
window = sg.Window("Excel表格数据处理", layout)

while True:
    event, values = window.read()
    if event is None or event == "退出":
        break
    if event == "开始":
        Python_Excel_Data_Processing(values["file_path"], values["folder_name"])
    if event == "选择Excel文件":
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            window["file_path"].update(file_path)
        root.destroy()
window.close()
