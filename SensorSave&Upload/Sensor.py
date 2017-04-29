#coding=utf-8

# 导入模块 datetime sys 以及Qt
import datetime
import time

import os;
import sys;

#*******************************************************************************
#                           陆超@2017-04-29
# Function Name  :  isDevExist
# Description    :  判断某文件是否存在
# Input          :  filePath    查找的路径
#                   keyWord     关键字
# Output         :  None
# Return         :  成功返回文件名  不存在 0
#*******************************************************************************

def isDevExist(filePath, keyWord):

    # 执行shell命令
    output = os.popen(filePath)
    out    = output.readlines()

    # 判断输出信息中是否有关键字
    for i in out:
        if (keyWord in i.strip()):
            #print(i.strip())
            return i.strip()
    return 0

print('Get Sensor Data and upload')


# 判断串口是否存在
serialPath = isDevExist('ls /dev', 'usbserial')
if ( serialPath != 0):
    print(serialPath)
else :
    print("没找到串口，程序结束！")
    sys.exit(0)

while 1 :
    print('Now is', datetime.datetime.now())
    time.sleep(1)

if __name__ == '__main__':
    print("主程序")


