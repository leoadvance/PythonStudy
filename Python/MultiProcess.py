#coding=utf-8
import multiprocessing
import time
import os

def Run(name):
    times = 1
    i = 0;
    print ('Process %s Start, which Father PID = %d' %(name, os.getppid()))
    while(i < 10):
        time.sleep(1)
        print ('This is %s PID = %d run_times = %d' %(name, os.getpid(), times))
        times += 1
        i += 1
    return

def Test():
    print ('多进程测试')
    proc1 = multiprocessing.Process(target=Run, args=('Process1',))
    proc2 = multiprocessing.Process(target=Run, args=('Process2',))
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    return