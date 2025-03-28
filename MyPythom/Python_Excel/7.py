import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

import random


class RollCallApp(QWidget):
    def __init__(self):
        super().__init__()

        self.students = ["蛋糕", "巧克力", "牛奶", "酸奶", "辣条", "麦丽素", "彩虹糖", "话梅糖", "年货瓜子"]

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('抽奖')

        self.checkboxes = []  # 存储学生复选框

        self.roll_call_button = QPushButton('抽奖', self)
        self.roll_call_button.clicked.connect(self.roll_call)

        # 使用水平布局排列学生复选框
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        for i, student in enumerate(self.students):
            checkbox = QCheckBox(student, self)
            self.checkboxes.append(checkbox)

            if i < len(self.students) // 2:
                hbox1.addWidget(checkbox)
            else:
                hbox2.addWidget(checkbox)

        # 添加全选复选框，并居中放置
        select_all_checkbox = QCheckBox('全选', self)
        select_all_checkbox.stateChanged.connect(self.select_all)
        hbox_center = QHBoxLayout()
        hbox_center.addStretch(1)
        hbox_center.addWidget(select_all_checkbox)
        hbox_center.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.roll_call_button)
        vbox.addLayout(hbox_center)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.resize_by_dpi_ratio(0)  # 设置放大比例
        self.set_font_size(12)  # 设置字体大小

        self.show()

    def resize_by_dpi_ratio(self, ratio):
        screen = QApplication.primaryScreen()
        dpi_ratio = screen.logicalDotsPerInch() / 96.0  # 获取屏幕DPI比例
        self.resize(int(self.width() * dpi_ratio * ratio), int(self.height() * dpi_ratio * ratio))

    def set_font_size(self, font_size):
        for checkbox in self.checkboxes:
            font = checkbox.font()
            font.setPointSize(font_size)
            checkbox.setFont(font)

    def select_all(self, state):
        # 全选复选框状态改变事件
        for checkbox in self.checkboxes:
            checkbox.setChecked(state == Qt.Checked)

    def roll_call(self):
        selected_students = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]

        if not selected_students:
            QMessageBox.information(self, '中奖结果', '请选择至少一个奖品！')
            return

        selected_student = random.choice(selected_students)
        QMessageBox.information(self, '中奖结果', f'抽到的奖品是: {selected_student}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RollCallApp()
    sys.exit(app.exec_())
