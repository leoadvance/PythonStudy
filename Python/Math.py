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

    print ("\r\n与或非运算")
    a = 0b0010
    b = 1
    print ("a & b = %02x, a | b = %02x, a ^ b = %02x, ~a = %02x"%(a & b, a | b,
                                                            a ^ b, ~a))
    print ("\r\n 学习is == 区别 == 判断值是否相等 is 判断是否是同一地址")
    a = 222222222222222222222
    b = 222222222222222222222
    c = b
    if a == c:
        print ("a = c")
    else:
        print ("a != c")

    if a is c:
        print ("a is c")
    else:
        print ("a c非同一地址")

    print ('\r\n学习 in not in的使用')
    a = 13
    l = [13, 14, "12312", '4324']
    print (l)

    if (a in l):
        print("a in l")
    else:
        print("a not in l")
    return