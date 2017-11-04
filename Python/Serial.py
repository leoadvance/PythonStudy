#coding=utf-8
import serial
import time
import threading
import os
import FileProcess

# mac linux下设备路径
DEVICE_PATH = '/dev'


#
# 串口接收程序，推荐被单独线程调用
#
# Parameters:
#       ser         - 已经打开的串口
#
#
# Returns:
#       None
#
def Serial_Rx(ser):
    print ('启动串口接收线程')

    # 生成log目录路径
    currentPath = os.path.join(os.path.abspath('.'), 'Serial_Log')

    # log文件名
    logFileName = time.strftime("%Y_%m_%d", time.localtime()) + '.log'
    logPath     = os.path.join(currentPath, logFileName)

    print (logPath)

    # 创建目录
    # FileProcess.DeletePath(currentPath)
    FileProcess.CreatePath(currentPath)

    # 打开log文件（可读可写）编码格式GBK
    SerialLog = open(logPath, 'a+', encoding='gbk')

    # 定位到文件末尾
    SerialLog.seek(0, 2)
    while(1):
        data = ser.readline()
        writeData = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + \
                    str(data.decode("gbk"))
        print (writeData)
        SerialLog.write(writeData)
        SerialLog.flush()

    return

#
# 串口测试程序
# 寻找设备列表里第一个串口打开并监听 数据保存在Serial_log文件夹下
# Parameters:
#       None
#
#
# Returns:
#       None
#
def Test():

    print('串口测试!')

    # 过滤现有串口
    SerialPath = FileProcess.GetDevicePath(DEVICE_PATH, 'tty.usb')

    # 打开第一个串口
    print ('打开串口' + SerialPath[0])
    ser = serial.Serial(SerialPath[0], 115200)
    if ser is None:
        print ('无法打开串口')
        return
    print (ser.isOpen())

    # 建立串口接收线程
    threadRx = threading.Thread(target=Serial_Rx, name = 'threadRx', args = (
        ser,))
    threadRx.start()



    # flush函数有问题，需要靠延时保证发送成功
    ser.write(b"1234567890\n")
    time.sleep(0.5)

    for i in range(10):
        ser.write(b"1234567890\n")
        time.sleep(0.2)
        i += 1
        # print (i)


    return threadRx