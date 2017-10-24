#coding=utf-8
import os
import sys
import chardet
import plotly.graph_objs as go
import DeleteFile as df
import plotly
import time
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
    CSVWriter.write('时间,甲醛,原始数据' + '\n')
    ListTimeX = []
    ListHCHOY = []

    fd = open(filename, 'r', encoding = CodeFormat)
    n = 0
    for line in fd:

        print (line)
        if len(line) > 10:

            listLen = line.split(']')

            # 删除起始的字符'【'
            list1 = listLen[0].__str__().split("[")

            # 提取时分秒
            h,m,s = list1[1].__str__().split(':')
            # print (h + m + s)

            ms = int(h) * 3600 * 1000 + int(m) * 60 * 1000 + float(s) * 1000
            ms = int(ms)

            # 记录首次偏移量
            if n == 0:
                TimsBase = ms
            n += 1
            ms -= TimsBase
            ms /= 1000

            # 记录时间ms
            ListTimeX.append(ms)
            # print (ListTimeX)
            CSVWriter.write(str(ms))

            # 提取数值
            listNum = listLen[1].__str__().split()
            # print (listNum)

            # 第4第5字节分别是高位和低位
            HighData = list(bytearray.fromhex(listNum[4]))
            LowData  = list(bytearray.fromhex(listNum[5]))
            # print (str(HighData[0]) + " " + str(LowData[0]))
            # 获取并记录甲醛值
            HCHOData = (HighData[0]* 256 + LowData[0]) / 1000.0
            # print (HCHOData)
            ListHCHOY.append(HCHOData)
            StrData = ',' + str(HCHOData)
            CSVWriter.write(StrData)
            CSVWriter.write(',' + listLen[1] + '\n')



    fd.close()
    CSVWriter.close()

    # 删除之前建立的.html文件
    df.DeleteFile(os.path.abspath('.'), '.html')

    # 画线+点
    trace0 = go.Scatter(
        x     = ListTimeX,
        y     = ListHCHOY,
        mode  = 'lines+markers',
        name  = 'HCHO',
        line=dict(
            color = ('rgb(205, 12, 24)'),
            width = 2)

    )

    data = [trace0]
    TitleLayout = dict(title='HCHO测试数据',
                  xaxis=dict(title='时间s'),
                  yaxis=dict(title='HCHO浓度mg/m3'),
                  )
    FileName = "Plotly_Draw_" + "Random_" + time.strftime("%Y_%m_%d_%H_%M_%S",
                                                          time.localtime()) + ".html"
    print(FileName)
    fig = dict(data=data, layout=TitleLayout)
    plotly.offline.plot(fig, filename=FileName)
    return