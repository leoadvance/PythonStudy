#coding=utf-8

# 导入系统模块
import sys
import os
import subprocess


class Shell(object):

#*******************************************************************************
#                           陆超@2016-12-06
# Function Name  :  GetMapCmd
# Description    :  获取map命令
# Input          :  要读取的文件名
# Output         :  None
# Return         :  map命令
#*******************************************************************************

    def GetMapCmd(fileName):

        sourceFileTypeCmd = "ffmpeg -i " + fileName

        # 获取文件类型
        print ("获取文件类型cmd：" + sourceFileTypeCmd)
        shellFileType = subprocess.getoutput(sourceFileTypeCmd)

        # 默认不包含字幕
        needVideo    = False
        needAudio    = False
        needSubtitle = False
        for line in shellFileType.split("\n"):

            # 找到Stream 那行
            if "Stream" in line:
                if "Video" in line:
                    needVideo = True
                    print ("包含视频：" + line)

                elif "Audio" in line:
                    needAudio = True
                    print ("包含音频：" + line)

                elif "Subtitle" in line:
                    needSubtitle = True
                    print ("包含字幕：" + line)

        mapCmd = ""
        if needSubtitle == True:
            mapCmd += " -map 0:s"
        if needAudio    == True:
            mapCmd += " -map 0:a"
        if needVideo    == True:
            mapCmd += " -map 0:v"

        print ("mapCmd" + mapCmd)
        return mapCmd

#*******************************************************************************
#                           陆超@2016-12-10
# Function Name  :  turnToH265
# Description    :  转换目录下文件至本目录下H265文件夹
# Input          :  self 类实体
# Output         :  None
# Return         :  None
#*******************************************************************************
    def turnToH265(FindPath):

        # 目标目录
        ChangeDirectory = "/H265"
        H265Sign        = ".H265.mp4"
        H265Directory = FindPath + ChangeDirectory

        FileNames     = os.listdir(FindPath)
        #print(FileNames)
        for i in FileNames:

            # 获取文件路径
            sonDirectoryPath = os.path.join(FindPath, i)

            # 是目录
            if os.path.isdir(sonDirectoryPath):

                print("发现子文件夹：" + sonDirectoryPath);
                Shell.turnToH265(sonDirectoryPath)

            # 判断后缀并输出输出文件名
            elif (os.path.splitext(i)[1] == ".mkv" or
                  os.path.splitext(i)[1] == ".mp4" or
                  os.path.splitext(i)[1] == ".mov" or
                  os.path.splitext(i)[1] == ".MOV" or
                  os.path.splitext(i)[1] == ".m4v" or
                  os.path.splitext(i)[1] == ".ts"):

                # 文件名
                filename     = os.path.join(i)

                # 带路径文件名
                fullfilename = os.path.join(FindPath, i)

                # 判断是否为转换后文件
                if H265Sign in filename:
                    print ("该文件已经转换过，跳过……")
                    continue

                # 创建转换后目录
                if os.path.exists(H265Directory) == False:
                    os.mkdir(H265Directory)
                    print("创建目录：" + H265Directory)

                # 分离文件名和扩展
                filenameHead, filenamExt = os.path.splitext(filename)
                print("文件名：" + filename + " 文件头:" + filenameHead + " 扩展名:" + filenamExt)

                # 源文件 和 目标文件
                sourceFile        = '"' + FindPath + "/" + filename + '"'
                destinationFile   = '"' + FindPath + ChangeDirectory + "/" + filenameHead + H265Sign + '"'

                # 获取map命令
                mapCmd = Shell.GetMapCmd(sourceFile)
                # 组合成想要的命名 用""防止空格
                shellcmd = ("ffmpeg -i " +
                            sourceFile + mapCmd +
                            " -c:v libx265 -preset medium -crf 23 " +
                            destinationFile )

                print(shellcmd)
                os.system(shellcmd)

                '''
                # 创建该文件
                newFilePath = FindPath + "/" + filenameHead + ".H265.mp4"
                f = open(newFilePath, 'w')
                f.close();
                print("创建新文件：" + newFilePath)
                '''
        return

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
        FindPath  = "/Users/LEO/Desktop"
        Shell.turnToH265(FindPath)
