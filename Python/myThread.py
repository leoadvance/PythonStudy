#coding=utf-8
import threading
import time
import Qt5
class myThread(threading.Thread):

    # 初始化函数
    def __init__(self, threadID, threadName, counter):
        threading.Thread.__init__(self)
        self.threadID   = threadID
        self.threadName = threadName
        self.counter    = counter

    def run(self):
        print("开始线程：" + self.name)
        print("结束线程：" + self.name)


def threadLoop(n):
    i = 0
    print ('Thread start which name is %s' %(threading.current_thread().name))
    while n:
        n -= 1
        i += 1
        time.sleep(1)
        print ('当前线程 %s 运行次数 = %d' %(threading.current_thread().name, i))

    print ('线程结束!')
    return

def threadqt():
    i = 0
    print ('Thread start which name is %s' %(threading.current_thread().name))
    result = Qt5.Qt_Test()

    print ('线程结束!')
    return

def threadTest():

    # 创建线程
    thread1  = threading.Thread(target = threadLoop, name= 'Thread_1', args=(5,))
    thread2  = threading.Thread(target = threadLoop, name= 'Thread_2', args=(5,))
    threadQt = threading.Thread(target = threadqt, name='Thread_Qt', args=())
    thread1.start()
    thread2.start()
    threadQt.start()

    # 等待线程结束 timeout 超时时间
    thread1.join(timeout = 1.5)

    print("线程1超时！")

    # 从运行到join起算超时时间 单位s
    thread2.join(timeout = 2)
    print("线程2超时！")

    return