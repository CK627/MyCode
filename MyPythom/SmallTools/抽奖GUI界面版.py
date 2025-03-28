import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QCheckBox, QPushButton, QVBoxLayout, QGridLayout,
    QHBoxLayout, QLineEdit, QMessageBox, QLabel
)
from PyQt5.QtCore import Qt
import secrets


class RollCallApp(QWidget):
    def __init__(self):
        super().__init__()

        self.students = ["蛋糕", "巧克力", "牛奶", "酸奶", "辣条", "麦丽素", "彩虹糖", "话梅糖", "年货瓜子"]
        self.updating = False
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('抽奖程序')

        self.checkboxes = []

        self.roll_call_button = QPushButton('抽奖', self)
        self.roll_call_button.clicked.connect(self.roll_call)

        self.select_all_checkbox = QCheckBox('全选', self)
        self.select_all_checkbox.stateChanged.connect(self.select_all)

        self.add_item_input = QLineEdit(self)
        self.add_item_input.setPlaceholderText("输入奖品名称")
        self.add_item_button = QPushButton('添加奖品', self)
        self.add_item_button.clicked.connect(self.add_item)

        self.clear_button = QPushButton('清空选择', self)
        self.clear_button.clicked.connect(self.clear_selection)

        self.grid_layout = QGridLayout()
        self.update_checkboxes()

        vbox = QVBoxLayout()
        vbox.addWidget(self.roll_call_button)
        vbox.addWidget(self.select_all_checkbox)

        hbox_add_item = QHBoxLayout()
        hbox_add_item.addWidget(self.add_item_input)
        hbox_add_item.addWidget(self.add_item_button)

        vbox.addLayout(hbox_add_item)
        vbox.addWidget(self.clear_button)
        vbox.addLayout(self.grid_layout)

        self.setLayout(vbox)

        self.resize_by_dpi_ratio(0.5)
        self.set_font_size(12)

        self.show()

    def update_checkboxes(self):  # 更新复选
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.checkboxes.clear()
        for i, student in enumerate(self.students):
            checkbox = QCheckBox(student, self)
            checkbox.stateChanged.connect(self.update_select_all_status)  # 添加状态监听
            self.checkboxes.append(checkbox)
            row, col = divmod(i, 3)
            self.grid_layout.addWidget(checkbox, row, col)

    def resize_by_dpi_ratio(self, ratio):  # 窗口
        screen = QApplication.primaryScreen()
        dpi_ratio = screen.logicalDotsPerInch() / 96.0
        self.resize(int(self.width() * dpi_ratio * ratio), int(self.height() * dpi_ratio * ratio))

    def set_font_size(self, font_size):  # 字体
        for checkbox in self.checkboxes:
            font = checkbox.font()
            font.setPointSize(font_size)
            checkbox.setFont(font)

    def select_all(self, state): # 全选
        if self.updating:
            return  # 如果正在更新状态，直接返回

        self.updating = True  # 设置标志，防止冲突
        for checkbox in self.checkboxes:
            checkbox.setChecked(state == Qt.Checked)
        self.updating = False  # 恢复标志

    def update_select_all_status(self):
        if self.updating:
            return

        self.updating = True
        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes)
        if all_checked:
            self.select_all_checkbox.setCheckState(Qt.Checked)
        elif any_checked:
            self.select_all_checkbox.setCheckState(Qt.PartiallyChecked)
        else:
            self.select_all_checkbox.setCheckState(Qt.Unchecked)
        self.updating = False

    def roll_call(self):  # 抽奖逻辑
        selected_students = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]

        if not selected_students:
            QMessageBox.warning(self, '抽奖结果', '请选择至少一个奖品！')
            return

        selected_student = secrets.choice(selected_students)
        result_label = QLabel(f'🎉 恭喜抽到的奖品是: <b style="color: green;">{selected_student}</b>')
        result_label.setAlignment(Qt.AlignCenter)

        result_box = QMessageBox(self)
        result_box.setWindowTitle("中奖结果")
        result_box.layout().addWidget(result_label)
        result_box.exec_()

    def add_item(self):  # 添加
        new_item = self.add_item_input.text().strip()
        if not new_item:
            QMessageBox.warning(self, '添加奖品', '奖品名称不能为空！')
            return
        if new_item in self.students:
            QMessageBox.warning(self, '添加奖品', '奖品已存在！')
            return

        self.students.append(new_item)
        self.update_checkboxes()
        self.add_item_input.clear()

    def clear_selection(self):  # 清空
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RollCallApp()
    sys.exit(app.exec_())