import datetime

import sys
from PyQt5 import QtWidgets, QtCore
print('Hello')
print('Hi Python this is Leo')
print('Now is',datetime.datetime.now(),'We Right the first code')

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec_())