#coding=utf-8
import os
import sys
import chardet

import DeleteFile as df

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

# 获取编码格式
def JudgeCodingFormat(filename):

    # 二进制方式读取文件 判断文件格式
    fd = open(filename, 'rb')
    result = chardet.detect(fd.read(100))
    print (filename + "的编码格式 = " + result['encoding'])
    fd.close()

    return result['encoding']

def LogProcess():

    print ('\r\nLog处理学习！处理当前路径下Log')

    filename = GetLogFile()

    if (filename == 'NULL'):
        return

    print ('系统默认编码格式 = ' + sys.getdefaultencoding())
    print ('打开log文件 %s', filename)

    # 获取编码格式
    CodeFormat =JudgeCodingFormat(filename)

    df.DeleteFile(os.path.abspath('.'), '.csv')

    # fd = open(filename, 'r', encoding = CodeFormat)
    # for line in fd:
    #     print (line)
    #
    # fd.close()
    return