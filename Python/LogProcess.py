#coding=utf-8
import os


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

    print ('打开log文件 %s', filename)
    fd = os.open(filename, os.O_RDONLY)

    os.close(fd)
    return