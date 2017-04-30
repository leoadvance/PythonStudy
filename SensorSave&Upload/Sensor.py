#coding=utf-8

# 导入模块 datetime sys 以及Qt
import datetime
import time

import os;
import sys;


#------------------------------ 宏定义 -----------------------------------------#
serialFindPath      = '/dev'                                            # 串口查找目录
serialFindKeyword   = 'usbserial'                                       # 串口查找关键词

#*******************************************************************************
#                           陆超@2017-04-29
# Function Name  :  isFileExist
# Description    :  判断某文件是否存在
# Input          :  filePath    查找的路径
#                   keyWord     关键字
# Output         :  None
# Return         :  成功返回文件名  不存在 0
#*******************************************************************************
def isFileExist(filePath, keyWord):

    # 执行shell命令
    output = os.popen(filePath)
    out    = output.readlines()

    # 判断输出信息中是否有关键字
    for i in out:
        if (keyWord in i.strip()):
            #print(i.strip())
            return i.strip()
    return 0

#*******************************************************************************
#                           陆超@2017-04-29
# Function Name  :  isSerialExist
# Description    :  判断串口是否存在
# Input          :  None
# Output         :  None
# Return         :  成功返回文件名  退出结束程序
#*******************************************************************************
def isSerialExist(serialFindPath, serialFindKeyword):

    # 阻止命令
    serialFindPathLs = 'ls ' + serialFindPath
    serialPath       = isFileExist(serialFindPathLs, serialFindKeyword)
    if ( serialPath != 0):
        return serialFindPath + '/' + serialPath
    else :
        print("没找到串口，程序结束！")
        sys.exit(0)


print('Get Sensor Data and upload')


# 判断串口是否存在
serialPath = isSerialExist(serialFindPath, serialFindKeyword)
print(serialPath)


while 1 :
    print('Now is', datetime.datetime.now())
    time.sleep(1)

if __name__ == '__main__':
    print("主程序")


