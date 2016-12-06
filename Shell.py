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

        # 遍历目录下文件
        FindPath = "/Users/LEO/Desktop/第一滴血 1080P"
        FileNames=os.listdir(FindPath)
        print(FileNames)
        for i in FileNames:
            # 判断后缀并输出输出文件名
            if os.path.splitext(i)[1] == ".mkv":

                # 文件名
                filename     = os.path.join(i)

                # 文件与路径名
                fullfilename = os.path.join(FindPath, i)

                # 替换空格
                fullfilenameshell = fullfilename.replace(' ', '\ ')
                # print(filename)
                # print(fullfilename)

                # 组合成想要的命名
                shellcmd = "ffmpeg -i " + fullfilenameshell + " -c:v libx265 -preset medium -crf 28 -c:a aac -b:a 384k " + fullfilenameshell

                # 删除多余.mkv 
                shellcmd = shellcmd.rstrip(".mkv")
                shellcmd += ".mp4"
                print(shellcmd)
                os.system(shellcmd)

        a = "ls"
        b = " -l"
        c = a + b
        subprocess.call(c, shell=True)
        print(
            "-------------------------- shell测试 ----------------------------")
