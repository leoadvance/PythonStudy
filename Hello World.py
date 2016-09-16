#coding=utf-8

# 导入模块 datetime sys 以及Qt
import datetime
import sys

from PyQt5 import QtWidgets

'''---------------------------------------------------------------------------------------------------------------------
*
* 数据类型测试
* 输出常用变量型号
*
---------------------------------------------------------------------------------------------------------------------'''

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

'''---------------------------------------------------------------------------------------------------------------------
*
* dir
* 查看模块，变量的属性和方法
*
---------------------------------------------------------------------------------------------------------------------'''

print(dir(a))


print('Hello！')
print('Hi Python this is Leo！')
print('Now is',datetime.datetime.now(),'We Right the first code')



app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec_())