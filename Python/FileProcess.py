#coding=utf-8

import os

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
    if os.path.exists(Path) is False:
        print('目录不存在，创建目录 ' + Path)
        os.makedirs(Path)
    else:
        print('目录 %s 存在' % (Path,))

    return