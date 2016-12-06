#coding=utf-8

#导入系统模块
import sys
import os

#引入子进程 管理shell
import subprocess

class Shell(object):

#*******************************************************************************
#                           陆超@2016-12-06
# Function Name  :  Test
# Description    :  shell学习
# Input          :  self 类实体
# Output         :  None
# Return         :  None
#*******************************************************************************

    def Test(self):

        print(self)
        print(self.__class__)

        #遍历目录下文件
        FindPath = "/Users/LEO/Desktop/第一滴血 1080P"
        FileNames=os.listdir(FindPath)
        print(FileNames)
        for fn in FileNames:
            #输出文件名
            fullfilename = os.path.join(fn)
            print(fullfilename)

        a = "ls"
        b = " -l"
        c = a + b
        subprocess.call(c, shell=True)
        print(
            "-------------------------- shell测试 ----------------------------")
