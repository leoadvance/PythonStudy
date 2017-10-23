#coding=utf-8
import os
import sys
import chardet
import time
import csv
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

    # 删除之前建立的.csv文件
    df.DeleteFile(os.path.abspath('.'), '.csv')

    # CSVWriter = csv.writer(open("log.csv", 'w'))
    CSVWriter = open("log.csv", 'w', encoding='gbk')
    CSVWriter.write('时间,甲醛' + '\n')
    ListTimeX = []
    listy = []
    fd = open(filename, 'r', encoding = CodeFormat)
    n = 0
    for line in fd:

        print (line)
        if len(line) > 10:

            list = line.split(']')

            # 删除起始的字符'【'
            list1 = list[0].__str__().split("[")

            # 提取时分秒
            h,m,s = list1[1].__str__().split(':')
            # print (h + m + s)

            ms = int(h) * 3600 * 1000 + int(m) * 60 * 1000 + float(s) * 1000
            ms = int(ms)

            if n == 0:
                TimsBase = ms
            ms -= TimsBase

            # 记录时间ms
            ListTimeX.append(ms)
            # print (ListTimeX)
            a = str(ms)
            print(ms)
            CSVWriter.write(a)
            CSVWriter.write('\n')

            print (list[1])
            n += 1

    fd.close()
    CSVWriter.close()
    return