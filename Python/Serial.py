#coding=utf-8
import serial
import time

def Test():

    print('串口测试!')

    ser = serial.Serial('/dev/tty.usbserial-3', 115200)
    ser.parity = serial.PARITY_NONE
    print (ser.isOpen())
    # # 设置读取超时时间 0.5s
    # ser.timeout = 2
    # print (n)
    print(ser)

    # ser.write("1234554563453".encode('gbk'))

    # flush函数有问题，需要靠延时保证发送成功
    ser.write(b"1234567890\n")
    time.sleep(0.5)

    for i in range(10):
        ser.write(b"1234567890\n")
        time.sleep(0.2)
        i += 1;
        print (i)


    return