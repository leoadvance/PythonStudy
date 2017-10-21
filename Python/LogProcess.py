#coding=utf-8
import os
import sys
import chardet


# 文件编码格式
FILE_ENCODE = 'utf-8'

def GetLogFile():

    print('打印当前目录下文件')
    listfile = os.listdir()
    print(listfile)

    print('过滤.log文件')

    for filename in listfile:
        if filename.endswith('.log'):
            print(filename)
            return filename
    return 'NULL'

def LogProcess():

    print ('\r\nLog处理学习！处理当前路径下Log')

    filename = GetLogFile()

    if (filename == 'NULL'):
        return

    print ('系统默认编码格式 = ' + sys.getdefaultencoding())
    print ('打开log文件 %s', filename)

    # 二进制方式读取文件 判断文件格式
    fd = open(filename, 'rb')
    result = chardet.detect(fd.read(100))
    print ("读取的编码格式 = " + result['encoding'])
    fd.close

    fd = open(filename, 'r', encoding = result['encoding'])
    for line in fd:
        print (line)

    fd.close()
    return