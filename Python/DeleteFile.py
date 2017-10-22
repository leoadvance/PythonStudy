#coding=utf-8

import os
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