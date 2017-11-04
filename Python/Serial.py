#coding=utf-8
import serial
import time
import threading
import os
import FileProcess
import chardet
# 串口接收任务
def Serial_Rx(ser):
    print ('启动串口接收线程')

    # 获取当前路径
    currentPath = os.path.abspath('.')
    currentPath += '/Serial_Log'

    # log文件名
    logPath = currentPath + time.strftime("/%Y_%m_%d",
                                          time.localtime()) + '.log'

    print (logPath)

    # 创建目录
    # FileProcess.DeletePath(currentPath)
    FileProcess.CreatePath(currentPath)

    # 打开log文件（可读可写）编码格式GBK
    SerialLog = open(logPath, 'a+', encoding='gbk')

    # 定位到文件末尾
    SerialLog.seek(0, 2)
    print (currentPath)
    while(1):
        data = ser.readline()
        writeData = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + \
                    str(data.decode("gbk"))
        print (writeData)
        SerialLog.write(writeData)
        SerialLog.flush()

    return

def Test():

    print('串口测试!')

    ser = serial.Serial('/dev/tty.usbserial-2', 115200)
    if ser is None:
        print ('无法打开串口')
        return
    print (ser.isOpen())

    # 建立串口接收线程
    threadRx = threading.Thread(target=Serial_Rx, name = 'threadRx', args = (
        ser,))
    threadRx.start()

    # # 设置读取超时时间 0.5s
    # ser.timeout = 2
    # print (n)


    # ser.write("1234554563453".encode('gbk'))

    # flush函数有问题，需要靠延时保证发送成功
    ser.write(b"1234567890\n")
    time.sleep(0.5)

    for i in range(10):
        ser.write(b"1234567890\n")
        time.sleep(0.2)
        i += 1;
        # print (i)


    return threadRx