#coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

def Qt_Test(QMainWindow):


    print("Qt测试")


    def __init__(self):

        #print("Qt测试")
        app = QApplication(sys.argv)
        super().__init__()
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()
        sys.exit(app.exec_())




