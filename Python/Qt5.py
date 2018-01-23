#coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class Qt_Test(QMainWindow):


    def __init__(self):

        print("Qt测试")
        app = QApplication(sys.argv)
        super().__init__()
        self.initUI()
        sys.exit(app.exec_())
        return

    def initUI(self):
        self.statusBar().showMessage('Hello World')
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Qt Study')
        self.show()
        return



