#coding=utf-8

# 导入模块 datetime sys 以及Qt
import datetime
import sys

#from PyQt5 import QtWidgets


#--------------------------------- 数据类型测试 ----------------------------------
print ("-------------------------- 数据类型测试演示 ----------------------------")
a = 10
b = 1.1
c = True
d = '221'

# int型
print ("a = 10,    a = ", type(a))

# float型
print ("b = 1.1,   b = ", type(b))

# bool型
print ("c = True,  c = ", type(c))

# str型
print ("d = '221', d = ", type(d))

# 字符串变整型
print(int(d) + a)

# 整型变字符串
print(str(a) + d)

#--------------------------------- 数学操作符 -----------------------------------
print ("--------------------------- 数学操作符演示 -----------------------------")
print ("指数 2  ** 3 =", 2 ** 3)
print ("取余 22 %  3 =", 22 % 3)
print ("整除 22 // 3 =", 22 // 3)
print ("除法 22 /  3 =", 22 / 3)
print ("乘法 22 *  3 =", 22 * 3)
print ("加法 22 +  3 =", 22 + 3)
print ("减法 22 -  3 =", 22 - 3)

#------------------------- dir 查看模块，变量属性和方法 ---------------------------

print(dir(a))

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
print('Now is',datetime.datetime.now(),'We Right the first code')


"""
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec_())
"""
