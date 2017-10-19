#coding=utf-8
import os
import sys

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

    print (sys.getdefaultencoding())
    print ('打开log文件 %s', filename)
    fd = open(filename, 'r', encoding = FILE_ENCODE)
    for line in fd:
        print (line)

    fd.close()
    return