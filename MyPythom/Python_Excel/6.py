import os
import sys
import threading

import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QPushButton, QLineEdit, QLabel, QTextEdit, QVBoxLayout, QWidget, QCheckBox, QHBoxLayout, QStackedWidget

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


class DataProcessor:
    def __init__(self):
        pass

    @staticmethod
    def acquisition_time(df_time):
        df_time.loc[:, '时间'] = pd.to_datetime(df_time['时间'])
        min_date = df_time['时间'].min()
        max_date = df_time['时间'].max()
        min_max_dates = f'{min_date.strftime("%Y-%m-%d")}-{max_date.strftime("%Y-%m-%d")}'
        return min_max_dates

    @staticmethod
    def normalize_department(department):
        cm = college_mapping
        for full_name, abbreviations in cm.items():
            for abbreviation in abbreviations:
                if abbreviation in department:
                    return full_name
        return department

    @staticmethod
    def process_category_data_colleget(df, category, output_folder):
        category_df = df[df["部门"] == category]
        row_count = len(category_df)
        output_file = os.path.join(output_folder, f'{category} 共打卡{row_count}次.xlsx')
        category_df.to_excel(output_file, index=False, engine='openpyxl')

    @staticmethod
    def process_category_data_mentor(df, category, output_folder):
        category_df = df[df["导师"] == category]
        row_count = len(category_df)
        output_file = os.path.join(output_folder, f'{category} 共打卡{row_count}次.xlsx')
        category_df.to_excel(output_file, index=False, engine='openpyxl')


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Excel数据处理')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget(self)

        department_page = QWidget()
        self.create_department_page(department_page)
        teacher_page = QWidget()
        self.create_teacher_page(teacher_page)

        self.stacked_widget.addWidget(department_page)
        self.stacked_widget.addWidget(teacher_page)

        layout = QVBoxLayout()

        self.input_fields = []

        file_path_layout = QHBoxLayout()
        self.create_label(file_path_layout, '选择Excel文件:')
        input_field = self.create_input_field(file_path_layout)
        self.create_browse_button(file_path_layout)
        layout.addLayout(file_path_layout)

        # Append the input field to the list
        self.input_fields.append(input_field)

        layout.addWidget(self.stacked_widget)

        self.mode_button = QPushButton('选择部门', self)
        self.mode_button.clicked.connect(self.toggle_mode)
        layout.addWidget(self.mode_button)

        new_folder_name_layout = QHBoxLayout()
        self.create_label(new_folder_name_layout, '新建文件夹名称:')
        self.create_input_field(new_folder_name_layout, '整理')
        layout.addLayout(new_folder_name_layout)

        buttons_layout = QHBoxLayout()
        self.create_button(buttons_layout, '开始', self.processing_college_data)
        self.create_button(buttons_layout, '退出', self.close)
        layout.addLayout(buttons_layout)

        self.log_text = QTextEdit(self)
        layout.addWidget(self.log_text)

        self.central_widget.setLayout(layout)

        self.current_mode = 0  # 初始为选择部门

        self.select_all_button = None  # 添加全选按钮属性

    def create_department_page(self, page):
        department_layout = QVBoxLayout()
        self.list_widget_department = self.create_list_widget(department_layout, '选择部门:', ["23级动漫制作技术1班","22级药学3班","艺术学院","23级软件技术班","23计算机应用1班","20级园林技术班","23级航一班宋增华","护理学院","建筑工程学院","21信息强化1班",
 "22物联网技术","23级物联网技术","23级计算机网络技术","21级计算机2班","22计算机应用4班","22级医学检验技术4班","机电工程学院","护理学院","22级园林技术班赵怀杰","22级药学2班","22级医学影像技术1班",
 "22级酒店邱萍","机电工程学院","机电工程学院","22医学影像技术5班"])
        department_select_all_button = self.create_select_all_button(department_layout, '全选部门')
        department_select_all_button.clicked.connect(lambda: self.select_all_items(self.list_widget_department, department_select_all_button))
        page.setLayout(department_layout)

    def create_button(self, layout, text, button_func):
        button = QPushButton(text, self)
        button.clicked.connect(button_func)
        layout.addWidget(button)


    def create_list_widget(self, layout, label_text, items):
        label = QLabel(label_text, self)
        layout.addWidget(label)
        list_widget = QListWidget(self)
        list_widget.addItems(items)
        list_widget.setSelectionMode(QListWidget.MultiSelection)
        layout.addWidget(list_widget)
        return list_widget

    def toggle_mode(self):
        # 清除选择部门和选择导师模式下的选项
        if self.current_mode == 0:
            self.list_widget_department.clearSelection()
        else:
            self.list_widget_teacher.clearSelection()

        # 清除全选按钮的状态
        if self.select_all_button is not None:
            self.select_all_button.setChecked(False)

        # 切换选择部门和选择导师模式
        self.current_mode = (self.current_mode + 1) % 2
        if self.current_mode == 0:
            self.mode_button.setText('选择部门')
            self.stacked_widget.setCurrentIndex(0)
        else:
            self.mode_button.setText('选择导师')
            self.stacked_widget.setCurrentIndex(1)

    def create_label(self, layout, label_text):
        label = QLabel(label_text, self)
        layout.addWidget(label)

    def create_select_all_button(self, layout, button_text):
        select_all_button = QCheckBox(button_text, self)
        layout.addWidget(select_all_button)
        return select_all_button

    def create_browse_button(self, layout):
        button = QPushButton('浏览', self)
        button.clicked.connect(self.selectFile)
        layout.addWidget(button)

    def selectFile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, '选择Excel文件', '', 'Excel文件 (*.xlsx);;所有文件 (*)',
                                                   options=options)
        if file_path:
            self.input_fields[0].setText(file_path)

    def create_teacher_page(self, page):
        teacher_layout = QVBoxLayout()
        self.list_widget_teacher = self.create_list_widget(teacher_layout, '选择导师:', ["孙泽霖", "孙彤彤"])
        teacher_select_all_button = self.create_select_all_button(teacher_layout, '全选导师')
        teacher_select_all_button.clicked.connect(lambda: self.select_all_items(self.list_widget_teacher, teacher_select_all_button))
        page.setLayout(teacher_layout)

    def create_input_field(self, layout, default_text=''):
        input_field = QLineEdit(self)
        if default_text:
            input_field.setText(default_text)
        layout.addWidget(input_field)
        return input_field  # Return the input_field widget
    def selectfile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, '选择Excel文件', '', 'Excel文件 (*.xlsx);;所有文件 (*)',
                                                   options=options)
        if file_path:
            self.file_path_input.setText(file_path)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName()
        self.file_path.setText(file_path)

    def start_processing(self):
        file_path = self.file_path.text()
        folder_name = self.folder_name.text()
        selected_department = self.department_combo.currentText()
        selected_teacher = self.teacher_combo.currentText()

        dp = DataProcessor()
        dp.process_category_data_colleget(file_path, folder_name, selected_department)
        dp.process_category_data_mentor(file_path, folder_name, selected_teacher)

    def log(self, message):
        self.log_text.append(message)

    def processing_college_data(self):
        if self.current_mode == 0:
            selected_departments = [item.text() for item in self.list_widget_department.selectedItems()]
            self.file_path = self.file_path_input.text()
            folder_name = self.folder_name_input.text()
            selected_department = self.department_combo.currentText()
            self.log_text.clear()
            if not self.file_path:
                self.log('请选择一个Excel文件。')
                return

            try:
                df = pd.read_excel(self.file_path, engine='openpyxl')
                unique_categories = df["部门"].unique()
                original_file_directory = os.path.dirname(self.file_path)
                output_folder = os.path.join(original_file_directory, folder_name)
                os.makedirs(output_folder, exist_ok=True)

                threads = []

                for category in unique_categories:
                    normalized_category = DataProcessor.normalize_department(category.split(':')[0])
                    if selected_department != "全选" and selected_department != normalized_category:
                        continue
                    thread = threading.Thread(target=DataProcessor.process_category_data_colleget,
                                              args=(df, normalized_category, output_folder))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()
                if selected_department == "全选":
                    summary_data = []
                    for category in unique_categories:
                        category_df = df[df["部门"] == category]
                        row_count = len(category_df)
                        summary_data.append(
                            [DataProcessor.acquisition_time(category_df),
                             DataProcessor.normalize_department(category.split(':')[0]), row_count])

                    summary_df = pd.DataFrame(summary_data, columns=["时间", "学院", "打卡次数"])
                    summary_file_path = os.path.join(output_folder, '各学院打卡次数统计.xlsx')
                    summary_df.to_excel(summary_file_path, index=False, engine='openpyxl')

                self.log('处理完成！')

            except Exception as e:
                self.log(f'处理过程中出现错误：{str(e)}')
        else:
            selected_teachers = [item.text() for item in self.list_widget_teacher.selectedItems()]
            print("Selected Teachers:", selected_teachers)



    def processing_mentor_data(self):
        file_path = self.file_path_input.text()
        folder_name = self.folder_name_input.text()
        selected_teacher = self.teacher_combo.currentText()
        self.log_text.clear()
        if not file_path:
            self.log('请选择一个Excel文件。')
            return

        try:
            df = pd.read_excel(file_path, engine='openpyxl')
            unique_categories = df["导师"].unique()
            original_file_directory = os.path.dirname(file_path)
            output_folder = os.path.join(original_file_directory, folder_name)
            os.makedirs(output_folder, exist_ok=True)

            threads = []

            for category in unique_categories:
                normalized_category = DataProcessor.normalize_department(category.split(':')[0])
                if selected_teacher != "全选" and selected_teacher != normalized_category:
                    continue
                thread = threading.Thread(target=DataProcessor.process_category_data_mentor,
                                          args=(df, normalized_category, output_folder))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()
            if selected_teacher == "全选":
                summary_data = []
                for category in unique_categories:
                    category_df = df[df["导师"] == category]
                    row_count = len(category_df)
                    summary_data.append(
                        [DataProcessor.acquisition_time(category_df),
                         DataProcessor.normalize_department(category.split(':')[0]), row_count])

                summary_df = pd.DataFrame(summary_data, columns=["时间", "导师", "打卡次数"])
                summary_file_path = os.path.join(output_folder, '各学院打卡次数统计.xlsx')
                summary_df.to_excel(summary_file_path, index=False, engine='openpyxl')

            self.log('处理完成！')

        except Exception as e:
            self.log(f'处理过程中出现错误：{str(e)}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())
