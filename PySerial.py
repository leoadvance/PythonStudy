#coding=utf-8

#导入串口模块
import serial
import sys

class PySerial(object):

#*******************************************************************************
#                           陆超@2016-09-17
# Function Name  :  type_study
# Description    :  数据类型测试
# Input          :  self 类实体
# Output         :  None
# Return         :  None
#*******************************************************************************

    def Init(self):

        print(self)
        print(self.__class__)


        print(
            "-------------------------- 串口初始化 ----------------------------")

        ser = serial.Serial(port     = '/dev/cu.usbserial-A50285BI',
                            baudrate = 115200,
                            parity   = serial.PARITY_NONE,
                            stopbits = serial.STOPBITS_ONE,
                            bytesize = serial.EIGHTBITS,
                            rtscts   = False,
                            timeout  = 0)

        # 输出串口号
        print("connected to: " + ser.portstr)

        return ser
