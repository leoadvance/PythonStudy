#coding=utf-8
class MathStudy(object):

#*******************************************************************************
#                           陆超@2016-09-17
# Function Name  :  type_study
# Description    :  数据类型测试
# Input          :  self 类实体
# Output         :  None
# Return         :  None
#*******************************************************************************

	def type_study(self):

	    print(self)
	    print(self.__class__)


	    print(
	        "-------------------------- 数据类型测试演示 ----------------------------")
	    a = 10
	    b = 1.1
	    c = True
	    d = '221'

	    # int型
	    print("a = 10,    a = ", type(a))

	    # float型
	    print("b = 1.1,   b = ", type(b))

	    # bool型
	    print("c = True,  c = ", type(c))

	    # str型
	    print("d = '221', d = ", type(d))

	    # 字符串变整型
	    print(int(d) + a)

	    # 整型变字符串
	    print(str(a) + d)

	# end of def type_study(self):

#*******************************************************************************
#                           陆超@2016-09-17
# Function Name  :  math_study
# Description    :  数学操作符测试
# Input          :  self 类实体
# Output         :  None
# Return         :  None
#*******************************************************************************

	def math_study(self):
	    print(self)
	    print(self.__class__)

	    print(
	        "--------------------------- 数学操作符演示 -----------------------------")
	    print("指数 2  ** 3 =", 2 ** 3)
	    print("取余 22 %  3 =", 22 % 3)
	    print("整除 22 // 3 =", 22 // 3)
	    print("除法 22 /  3 =", 22 / 3)
	    print("乘法 22 *  3 =", 22 * 3)
	    print("加法 22 +  3 =", 22 + 3)
	    print("减法 22 -  3 =", 22 - 3)

	# end of def math_study(self):
