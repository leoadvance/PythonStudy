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

MULTIPLE = 1
timestart = time.time() * MULTIPLE


# 打印时间
print ("程序启动时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print (sys.platform)



# print必须带括号
Print.Print_Fun()

# 变量测试
Variable.VariableTest()
timeend = time.time() * MULTIPLE

# 运算符测试
Math.MathTest()

print ("开始时间" + str(timestart))
print ("结束时间" + str(timeend))
print ("运行时间" + str(timeend - timestart))


if __name__ == "__main__":
    print ("主程序")