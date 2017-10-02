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
    s *= 2
    print(s)

    print("\r\n替换字符串中某个字节")
    print("第一步，l1 = list(s), 转换字符串内容为list")
    l1 = list(s)
    print("第二步，l1[0] = 'a', 修改想要替换内容")
    l1[0] = 'a'
    print("第三步，s = "".join(11), 列表数据转存入字符串")
    s = "".join(l1)
    print(s)



    # 列表
    print ("\r\nlist列表测试:")
    l = ["234", 768476, 12.3, "Test"]
    print("print (l)")
    print (l)
    print("print (l[1:3])")
    print (l[1:3])
    print("l *= 2")
    l *= 2
    print("print (l)")
    print(l)
    print ("list内部成员除了可以改变数值，还是改变类型！")
    print("l[1] = \"abc\"")
    print("l[2] = 123.45")
    l[1] = "abc"
    l[2] = 123.45
    print("print (l)")
    print(l)

    print("\r\n实现列表插入功能：l.insert(1, 7878), 表示在原有位置1前插入数字7878")
    l.insert(1, 7878)
    print(l)


    # dictionary
    print ("\r\ndictionary 学习!")

    print ("dict = {}   声明字典")
    dict = {}
    dict[2] = "This is dict 2"

    tinydict = {1: "test1", "two": 1234}
    print (dict[2])
    print (tinydict.keys())
    print (tinydict.values())


    return
