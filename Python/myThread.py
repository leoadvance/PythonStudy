#coding=utf-8
import threading
class myThread(threading.Thread):

    # 初始化函数
    def __init__(self, threadID, threadName, counter):
        threading.Thread.__init__(self)
        self.threadID   = threadID
        self.threadName = threadName
        self.counter    = counter

    def run(self):
         print("开始线程：" + self.name)
         print("退出线程：" + self.name)