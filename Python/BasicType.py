#coding=utf-8
# 定义编码格式

#Numbers（数字）
#String（字符串）
#List（列表）
#Tuple（元组）
#Dictionary（字典）

# 通过import文件名引入其他文件内函数
import Print
import time
import Variable
import sys
import Math
import LEOCycle
import Draw
import PygalDraw

MULTIPLE = 1
timestart = time.time() * MULTIPLE


# 打印时间
print ("程序启动时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 输出系统运行平台
print (sys.platform)

if (sys.platform == 'win32'):
    print ('Windows平台运行')



# print必须带括号
Print.Print_Fun()

# 不定参数函数
Print.Print_Var(1,'123', 3)

# # 变量测试
# Variable.VariableTest()
#
# # 运算符测试
# Math.MathTest()
#
# # 循环测试
# LEOCycle.LEOCycleTest()

# 绘图测试
#Draw.DrawTest()

#PygalDraw.DrawTest()
timeend = time.time() * MULTIPLE
print ("开始时间" + str(timestart))
print ("结束时间" + str(timeend))
print ("运行时间" + str(timeend - timestart))


if __name__ == "__main__":
    print ("主程序")