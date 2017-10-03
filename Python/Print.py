#codingutf-8


# 函数以def开头 参数可省略 以冒号结尾 return返回
def Print_Fun():
    print ("Print 函数测试！")
    return

# 不定参数函数
def Print_Var(*vartuple):
    for var in vartuple:
        print (var)
    return