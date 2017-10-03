#coding=utf-8

def MathTest():

    print ("\r\n运算符测试！")

    a = 0x10
    print ("16进制输出")
    print ("a = 0x%x"%(a))
    print ("a = " + hex(a) + " " + "a = " + oct(a) + " " + "a = " + bin(a))

    print ("取余数运算 % （5.1 % 2.1）")
    a = 5.1
    b = 2.1
    print (a % b)

    print("取整运算 % （5.1 // 2.1）")
    print (a // b)
    return