# -*- coding = utf-8 -*-
# @Time:2023/2/18 11:30
# @Author:CK
# @File:2
# @Software:PyCharm
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget
    w = QWidget()
    # 设置标题
    w.setWindowTitle("看看我图标帅吗")
    # 设置图标
    w.setWindowIcon(QIcon('1.jpg'))
    # 显示QWidget
    w.show()

    app.exec()
