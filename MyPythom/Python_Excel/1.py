import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QCheckBox, QVBoxLayout, QLineEdit

class ExcelProcessingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel表格处理")
        self.setGeometry(100, 100, 400, 300)

        self.excel_path_btn = QPushButton("选择Excel文件", self)
        self.excel_path_btn.clicked.connect(self.get_excel_file)

        self.file_list = QCheckBox("多选/单选", self)

        self.toggle_button = QPushButton("切换框", self)
        self.toggle_button.clicked.connect(self.toggle_checkboxes)

        self.select_all_button = QPushButton("全选", self)
        self.select_all_button.clicked.connect(self.select_all)

        self.input_text = QLineEdit(self)

        self.start_button = QPushButton("开始", self)
        self.start_button.clicked.connect(self.start_processing)

        self.quit_button = QPushButton("退出", self)
        self.quit_button.clicked.connect(self.close)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.excel_path_btn)
        self.layout.addWidget(self.file_list)
        self.layout.addWidget(self.toggle_button)
        self.layout.addWidget(self.select_all_button)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.quit_button)
        self.setLayout(self.layout)

        self.checkbox_group1 = []
        self.checkbox_group2 = []

    def get_excel_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog.getOpenFileName(self, "选择Excel文件", "", "Excel Files (*.xlsx *.xls)", options=options)
        file_path = file_dialog[0]
        if file_path:
            print(f"Selected Excel file: {file_path}")

    def toggle_checkboxes(self):
        if self.file_list.isChecked():
            self.layout.removeWidget(self.toggle_button)
            self.layout.addWidget(self.select_all_button)
            self.file_list.setText("多选/单选")
        else:
            self.layout.removeWidget(self.select_all_button)
            self.layout.addWidget(self.toggle_button)
            self.file_list.setText("切换框")
        self.update()

    def select_all(self):
        for checkbox in self.checkbox_group1 + self.checkbox_group2:
            checkbox.setChecked(True)

    def start_processing(self):
        user_input = self.input_text.text()
        print(f"User input: {user_input}")
        # 进行Excel处理的代码可以在这里添加

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExcelProcessingApp()
    window.show()
    sys.exit(app.exec_())
