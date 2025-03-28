# -*- coding = utf-8 -*-
# @Time:2023/2/18 10:19
# @Author:CK
# @File:创建一个串窗口
# @Software:PyCharm
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)

w = QWidget()

w.setWindowTitle("后缀名添加与删除")
label = QLabel("后缀名添加与删除",w)
label.setGeometry(20,20,200,30)
label2 = QLabel("使用说明：\n点击“文件路径”可以弹出资源管理器选择文件夹\n鼠标悬浮在输入框有提示",w)
label2.setGeometry(20,50,400,60)
file_path = QLabel("文件路径",w)
file_path.setGeometry(20,130,200,40)
file_path_edit = QLineEdit(w)
file_path_edit.setPlaceholderText("请输入路径")
file_path_edit.setGeometry(100,130,250,40)
Suffix_name = QLabel("后缀名",w)
Suffix_name.setGeometry(20,160,40,40)
Suffix_name_edit = QLineEdit(w)
Suffix_name_edit.setPlaceholderText("请输入要添加或者更改的后缀名")
Suffix_name_edit.setGeometry(65,160,300,40)

btn = QPushButton("增加",w)
btn.setGeometry(20,300,60,60)
btn2 = QPushButton("删除",w)
btn2.setGeometry(80,300,60 ,60)
btn3 = QPushButton("退出", w)
btn3.setGeometry(145, 300, 60,60)

w.move(200,200)


w.show()
app.exec()