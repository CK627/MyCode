# -*- coding = utf-8 -*-
# @Time:2023/10/24 9:14
# @Author:CK
# @File:Python_Excel_NO.4
# @Software:PyCharm
import os
import threading

import PySimpleGUI as sg
import pandas as pd

# 学院全名和简称的映射
college_mapping = {
    "信息工程学院": ["信息工程", "信息工程学院"],
    "医药学院": ["医药", "医药学院"],
    "商学院": ["商", "商学院"],
    "基础学院": ["基础", "基础学院"],
    "外国语学院": ["外国语", "外国语学院"],
    "建筑工程学院": ["建筑", "建筑学院", "建筑工程学院"],
    "影视学院": ["影视", "影视学院"],
    "护理学院": ["护理", "护理学院"],
    "捷能学院": ["捷能", "捷能学院"],
    "旅游酒店管理学院": ["旅游学院", "旅游酒店管理学院"],
    "机电工程学院": ["机电", "机电学院"],
    "汽车工程学院": ["汽车", "汽车学院"],
    "笃志学院": ["笃志", "笃志学院"],
    "航空服务学院": ["航空", "航空学院"],
    "艺术学院": ["艺术", "艺术学院"]
}


def acquisition_time(df_time):
    df_time.loc[:, '时间'] = pd.to_datetime(df_time['时间'])
    min_date = df_time['时间'].min()
    max_date = df_time['时间'].max()
    min_max_dates = f'{min_date.strftime("%Y-%m-%d")}-{max_date.strftime("%Y-%m-%d")}'
    return min_max_dates


def normalize_department(department):
    for full_name, abbreviations in college_mapping.items():
        for abbreviation in abbreviations:
            if abbreviation in department:
                return full_name
    return department


def process_category_data(df, category, output_folder):
    category_df = df[df["部门"] == category]
    row_count = len(category_df)
    output_file = os.path.join(output_folder, f'{category} 共打卡{row_count}次.xlsx')
    category_df.to_excel(output_file, index=False, engine='openpyxl')


def process_teachers_data(df, category, output_folder):
    category_df = df[df["导师"] == category]
    row_count = len(category_df)
    output_file = os.path.join(output_folder, f'{category} 共打卡{row_count}次.xlsx')
    category_df.to_excel(output_file, index=False, engine='openpyxl')


def select_file():
    sg.theme("LightBlue2")
    folder_name_choices = [
        "全选",
        "23级动漫制作技术1班", "22级药学3班", "艺术学院", "23级软件技术班", "23计算机应用1班", "20级园林技术班",
        "23级航一班宋增华",
        "护理学院", "建筑工程学院", "21信息强化1班", "22物联网技术", "23级物联网技术", "23级计算机网络技术",
        "21级计算机2班",
        "22计算机应用4班", "22级医学检验技术4班", "机电工程学院", "护理学院", "22级园林技术班赵怀杰", "22级药学2班",
        "22级医学影像技术1班", "22级酒店邱萍", "机电工程学院", "机电工程学院", "22医学影像技术5班"
    ]
    folder_name_teacher = ["全选", "孙泽霖", "孙彤彤"]

    layout = [
        [sg.Text("Excel表格数据处理", size=(30, 1), justification="center", font=("Helvetica", 16))],
        [sg.Text("使用说明：\n分院和导员默认全选")],
        [sg.Text("选择Excel文件", size=(15, 1)), sg.Input(key='file_path', size=(40, 1)),
         sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), size=(10, 1))],
        [sg.Text("请选择部门", size=(15, 1)),
         sg.Listbox(values=folder_name_choices, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, default_values=["全选"],
                    size=(38, 5), key='department_choice')],
        [sg.Text("请选择导员", size=(15, 1)),
         sg.Listbox(values=folder_name_teacher, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, default_values=["全选"],
                    size=(38, 5), key='teacher_choice')],
        [sg.Text("新建文件夹名称", size=(15, 1)), sg.Input(key='folder_name', size=(40, 1), default_text='整理')],
        [sg.Button("学院--开始"), sg.Button("导员--开始"), sg.Button("退出")]
    ]

    window = sg.Window("Excel表格数据处理", layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "退出"):
            break
        if event == "学院--开始":
            file_path = values['file_path']
            folder_name = values['folder_name']
            selected_departments = values['department_choice']
            process_excel_data_department(file_path,folder_name,selected_departments)

        if event == "导员--开始":
            file_path = values["file_path"]
            folder_name = values['folder_name']
            selected_teachers = values['teacher_choice']
            process_excel_data_teacher(file_path, folder_name, selected_teachers)

    window.close()


def process_excel_data_department(file_path, folder_name, selected_departments):
    if not file_path:
        sg.popup_error("请选择一个Excel文件")
        return
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        unique_categories = df["部门"].unique()
        original_file_directory = os.path.dirname(file_path)
        output_folder = os.path.join(original_file_directory, folder_name)
        os.makedirs(output_folder, exist_ok=True)
        threads = []
        if "全选" in selected_departments:
            selected_departments = list(unique_categories)
        for category in unique_categories:
            normalized_category = normalize_department(category.split(':')[0])
            if not selected_departments or normalized_category in selected_departments:
                thread = threading.Thread(target=process_category_data,
                                          args=(df, normalized_category, output_folder))
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()
        if selected_departments:
            summary_data = []
            for category in selected_departments:
                category_df = df[df["部门"] == category]
                row_count = len(category_df)
                summary_data.append(
                    [acquisition_time(category_df), normalize_department(category.split(':')[0]), row_count])
            summary_df = pd.DataFrame(summary_data, columns=["时间", "部门", "打卡次数"])
            summary_file_path = os.path.join(output_folder, '选定部门打卡次数统计.xlsx')
            summary_df.to_excel(summary_file_path, index=False, engine='openpyxl')

        sg.popup("学院处理完成！", title="成功")
    except Exception as e:
        sg.popup_error(f"学院处理时出错: {str(e)}", title="错误")


def process_excel_data_teacher(file_path, folder_name, selected_teachers):
    if not file_path:
        sg.popup_error("请选择一个Excel文件")
        return
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        unique_categories = df["导师"].unique()
        original_file_directory = os.path.dirname(file_path)
        output_folder = os.path.join(original_file_directory, folder_name)
        os.makedirs(output_folder, exist_ok=True)
        threads = []
        if "全选" in selected_teachers:
            selected_teachers = list(unique_categories)
        for category in unique_categories:
            normalized_category = normalize_department(category.split(':')[0])
            if not selected_teachers or normalized_category in selected_teachers:
                thread = threading.Thread(target=process_teachers_data,
                                          args=(df, normalized_category, output_folder))
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()
        if selected_teachers:
            summary_data = []
            for category in selected_teachers:
                category_df = df[df["导师"] == category]
                row_count = len(category_df)
                summary_data.append(
                    [acquisition_time(category_df), normalize_department(category.split(':')[0]), row_count])
            summary_df = pd.DataFrame(summary_data, columns=["时间", "导员", "打卡次数"])
            summary_file_path = os.path.join(output_folder, '选定导员打卡次数统计.xlsx')
            summary_df.to_excel(summary_file_path, index=False, engine='openpyxl')

        sg.popup("导员处理完成！", title="成功")
    except Exception as e:
        sg.popup_error(f"导员处理时出错: {str(e)}", title="错误")


if __name__ == "__main__":
    select_file()