#coding=utf-8
import sys
import QtTest
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class Qt_Test(QMainWindow):


    def __init__(self):

        print("Qt测试")
        app = QApplication(sys.argv)
        super().__init__()
        # self.initUI()
        MainWindow = QMainWindow()
        ui = QtTest.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        return

    def initUI(self):

        return



