#coding=utf-8

# 导入模块 datetime sys 以及Qt
import datetime
import sys

from PyQt5 import QtWidgets

dir(sys)
print('Hello！')
print('Hi Python this is Leo！')
print('Now is',datetime.datetime.now(),'We Right the first code')

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec_())