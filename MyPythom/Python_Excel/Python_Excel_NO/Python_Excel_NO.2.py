# -*- coding = utf-8 -*-
# @Time:2023/10/20 6:59
# @Author:CK
# @File:Python_Excel_NO.抽奖GUI界面版.py
# @Software:PyCharm
import os
import PySimpleGUI as sg
import pandas as pd


def select_file():
    sg.theme("LightBlue2")
    layout = [[sg.Text("Excel表格数据处理", size=(30, 1), justification="center", font=("Helvetica", 16))],
              [sg.Text("使用说明：\n鼠标悬浮在输入框有提示")],
              [sg.Text("选择Excel文件", size=(15, 1)), sg.Input(key='file_path', size=(40, 1)),
               sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), size=(10, 1))],
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


def process_excel_data(file_path, folder_name):
    df = pd.read_excel(file_path, engine='openpyxl')
    unique_categories = df["部门"].unique()
    original_file_directory = os.path.dirname(file_path)
    output_folder = os.path.join(original_file_directory, folder_name)
    os.makedirs(output_folder, exist_ok=True)

    def acquisition_time(df_time):
        df_time.loc[:, '时间'] = pd.to_datetime(df_time['时间'])
        min_date = df_time['时间'].min()
        max_date = df_time['时间'].max()
        min_max_dates = f'{min_date.strftime("%Y-%m-%d")}-{max_date.strftime("%Y-%m-%d")}'
        return min_max_dates

    summary_data = []

    for category in unique_categories:
        category_df = df[df["部门"] == category]
        row_count = len(category_df)
        output_file = os.path.join(output_folder, f'{category} 共打卡{row_count}次.xlsx')
        category_df.to_excel(output_file, index=False, engine='openpyxl')
        summary_data.append([acquisition_time(category_df), category, row_count])

    summary_df = pd.DataFrame(summary_data, columns=["时间", "学院", "打卡次数"])
    summary_file_path = os.path.join(output_folder, '各学院打卡次数统计.xlsx')
    summary_df.to_excel(summary_file_path, index=False, engine='openpyxl')


if __name__ == "__main__":
    select_file()
