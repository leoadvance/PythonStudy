#coding=utf-8

import os
import shutil

'''
删除某类型文件文件

Parameters:
    FilePath    - 文件路径
    FileType    - 文件类型

Returns:
    None
        
'''
def DeleteFile(FilePath, FileType):

    print ('删除目录下某类型文件')
    print ('当前目录' + FilePath)
    listfile = os.listdir(FilePath)
    print(listfile)

    for filename in listfile:
        if filename.endswith(FileType):
            print(filename)
            os.remove(filename)

    return


'''
创建目录

Parameters:
    Path        - 目录路径


Returns:
    None

'''
def CreatePath(Path):
    # 创建目录
    if os.path.exists(Path) == False:
        print('目录不存在，创建目录 ' + Path)
        os.makedirs(Path)
    else:
        print('目录 %s 存在' % (Path,))

    return

'''
删除目录

Parameters:
    Path        - 目录路径


Returns:
    None

'''
def DeletePath(Path):
    # 删除目录
    if os.path.exists(Path) == True:
        print('目录存在，删除目录 ' + Path)
        shutil.rmtree(Path, True)


    return

#
# 删除目录
#
# Parameters:
#       Path        - 目录路径
#       KeyWords    - 设备关键字
#
# Returns:
#       设备路径
#
#
def GetDevicePath(Path, KeyWords):

    # 声明返回列表
    returnPath = []

    # 删除目录
    listfile = os.listdir(Path)

    # 遍历列表
    for fileName in listfile:
        filePath = os.path.join(Path, fileName)
        if KeyWords in fileName:
            print ('找到设备第' + str(len(returnPath) + 1) + '个设备 '+ fileName)
            returnPath.append(filePath)

    return returnPath