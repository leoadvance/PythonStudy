#coding=utf-8

def VariableTest():

    # 声明字符串变量s
    s = "123456"

    print ("\r\n字符串变量测试:")
    print ("print (s): " + s)
    print ("print (s[1:5]): " + s[1:5])

    # 变量可以直接通过加连接
    s += "hello"
    print(s)

    # 变量可以通过乘法倍增
    s *= 3
    print(s)


    # 列表
    print ("\r\nlist列表测试:")
    list = ["234", 768476, 12.3, "Test"]
    print("print (list)")
    print (list)
    print("print (list[1:3])")
    print (list[1:3])
    print("list *= 2")
    list *= 2
    print("print (list)")
    print(list)

    print ("list内部成员除了可以改变数值，还是改变类型！")
    print("list[1] = \"abc\"")
    print("list[2] = 123.45")
    list[1] = "abc"
    list[2] = 123.45
    print("print (list)")
    print(list)

    #b = list(s[0])

    #print (b)

    return
