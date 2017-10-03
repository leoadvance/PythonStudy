#coding=utf-8
import time
def LEOCycleTest():

    print ('\r\n循环测试')
    print ('while用于普通循环，for用于遍历内容')
    i = 0
    a = 0
    while (i < 2):
        print (i)
        i += 1
        for b in 'Python':
            print ('当前字母：', b)


    return