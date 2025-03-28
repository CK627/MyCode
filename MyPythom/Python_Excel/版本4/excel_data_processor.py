import os
import pandas as pd
import threading
import PySimpleGUI as sg  # 添加此行导入语句

# 学院全名和简称的映射
college_mapping = {
    "信息工程学院": ["信息工程", "信息工程学院"],
    "医药学院": ["医药", "医药学院"],
    # 添加其他学院的映射信息
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
    # 数据处理函数代码
    pass

def select_file():
    sg.theme("LightBlue2")
    folder_name_choices = ["分院", "导员"]
    layout = [
        [sg.Text("Excel表格数据处理", size=(30, 1), justification="center", font=("Helvetica", 16))],
        [sg.Text("使用说明：\n鼠标悬浮在输入框有提示")],
        [sg.Text("选择Excel文件", size=(15, 1)), sg.Input(key='file_path', size=(40, 1)),
         sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), size=(10, 1))],
        [sg.Text("筛选选项", size=(15, 1)),
         sg.Combo(folder_name_choices, default_value="分院", key='additional_option', size=(30, 1))],
        [sg.Text("新建文件夹名称", size=(15, 1)), sg.Input(key='folder_name', size=(40, 1), default_text='整理')],
        [sg.Button("开始"), sg.Button("退出")]
    ]

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

        for category in unique_categories:
            normalized_category = normalize_department(category.split(':')[0])
            thread = threading.Thread(target=process_category_data,
                                      args=(df, normalized_category, output_folder))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        summary_data = []
        for category in unique_categories:
            category_df = df[df["部门"] == category]
            row_count = len(category_df)
            summary_data.append([acquisition_time(category_df), normalize_department(category.split(':')[0]), row_count])

        summary_df = pd.DataFrame(summary_data, columns=["时间", "学院", "打卡次数"])
        summary_file_path = os.path.join(output_folder, '各学院打卡次数统计.xlsx')
        summary_df.to_excel(summary_file_path, index=False, engine='openpyxl')

        sg.popup("处理完成！", title="成功")
    except Exception as e:
        sg.popup_error(f"处理时出错: {str(e)}", title="错误")

if __name__ == "__main__":
    select_file()
