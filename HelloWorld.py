#coding=utf-8

# 导入模块 datetime sys 以及Qt
import datetime
import sys
from MathStudy import MathStudy
from PySerial import PySerial

from PyQt5 import QtWidgets

# 打印系统环境变量
print(sys.path)
aa = MathStudy()
aa.type_study()
aa.math_study()

UART = PySerial()

ser1 = UART.Init()

ser1.write('123'.encode('ascii'))




#------------------------- dir 查看模块，变量属性和方法 ---------------------------

print(dir(10))

#*******************************************************************************
#                           陆超@2016-09-17
# Function Name  :  imax
# Description    :  比较大小
# Input          :  a 待比较数据
#                   b 待比较数据
# Output         :  None
# Return         :  max value
#*******************************************************************************
print ("--------------------------- def 函数功能演示 ---------------------------")
def imax(a, b):
    if (a >= b):
        return a
    else:
        return b

# end of def imax (a, b)

print (imax(10, 5))

print('Hello！')
print('Hi Python this is Leo！')
print('Now is', datetime.datetime.now(), 'I Write the first code')



app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec_())
