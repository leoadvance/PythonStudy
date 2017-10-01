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


# 打印时间
print ("程序启动时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# print必须带括号
Print.Print_Fun()

Variable.VariableTest()