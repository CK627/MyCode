# -*- coding = utf-8 -*-
# @Time:2023/10/21 19:34
# @Author:ck
# @File:gui_interface
# @Software:PyCharm
import PySimpleGUI as sg

from excel_data_processor import process_excel_data


def select_file():
    sg.theme("LightBlue2")
    folder_name_choices = ["分院","导员"]
    layout = [[sg.Text("Excel表格数据处理", size=(30, 1), justification="center", font=("Helvetica", 16))],
              [sg.Text("使用说明：\n鼠标悬浮在输入框有提示")],
              [sg.Text("选择Excel文件", size=(15, 1)), sg.Input(key='file_path', size=(40, 1)),sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), size=(10, 1))],
              [sg.Text("筛选选项", size=(15, 1)),sg.Combo(folder_name_choices, default_value="分院", key='additional_option', size=(30, 1))],
              [sg.Text("新建文件夹名称", size=(15, 1)), sg.Input(key='folder_name', size=(40, 1), default_text='整理')],
              [sg.Button("开始"), sg.Button("退出")]]

    window = sg.Window("Excel表格数据处理", layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "退出"):
            break
        if event == "开始":
            file_path = values['file_path']
            folder_name = values['folder_name']
            process_excel_data(file_path, folder_name)

    window.close()

if __name__ == "__main__":
    select_file()
