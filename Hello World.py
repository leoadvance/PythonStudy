#coding=utf-8

# 导入模块 datetime sys 以及Qt
import datetime
import sys

from PyQt5 import QtWidgets


#--------------------------------- 数据类型测试 ----------------------------------

a = 10
b = 1.1
c = True
d = '221'

# int型
print (type(a))

# float型
print (type(b))

# bool型
print (type(c))

# str型
print (type(d))

# 字符串变整型
print(int(d) + a)

# 整型变字符串
print(str(a) + d)



"""----------------------- dir 查看模块，变量属性和方法 -------------------------"""
print(dir(a))

"""*****************************************************************************
*                           陆超@2016-09-17
* Function Name  :  ADDCheck
* Description    :  累加校验
* Input          :  unsigned int uiData     待比较数据
*                   unsigned char *ucsData  源数据地址
*                   int uiLen               源数据长度
* Output         :  None
* Return         :  相同返回0 不同返回-1
*****************************************************************************"""


print('Hello！')
print('Hi Python this is Leo！')
print('Now is',datetime.datetime.now(),'We Right the first code')



app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec_())