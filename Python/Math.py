#coding=utf-8

def MathTest():

    print ("\r\n运算符测试！")

    a = 0x10
    print ("16进制输出")
    print ("a = 0x%x"%(a))
    print ("a = " + hex(a) + " " + "a = " + oct(a) + " " + "a = " + bin(a))

    print ("\r\n取余数运算 % （5.1 % 2.1）")
    a = 5.1
    b = 2.1
    print (a % b)

    print("\r\n取整运算 % （5.1 // 2.1）")
    print (a // b)

    print("\r\n指数运算 % （2 ** 3）")
    a = 2
    b = 3
    print (a ** b)

    return