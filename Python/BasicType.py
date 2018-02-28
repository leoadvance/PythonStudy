#coding=utf-8
# 定义编码格式

#Numbers（数字）
#String（字符串）
#List（列表）
#Tuple（元组）
#Dictionary（字典）

# 通过import文件名引入其他文件内函数
import Print
import time
import Variable
import sys
import Math
import LEOCycle
import Draw
import PygalDraw
import LogProcess
import Serial
import MultiProcess
import myThread
import Qt5
import Algorithm

import itchat
import urllib3
import requests
# 登录微信
# itchat.auto_login()
# frends = itchat.get_friends(update=True)[0:]

MULTIPLE = 1
timestart = time.time() * MULTIPLE


# 打印时间
print ("程序启动时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 输出系统运行平台
print (sys.platform)

if (sys.platform == 'win32'):
    print ('Windows平台运行')



# print必须带括号
# Print.Print_Fun()

# 不定参数函数
Print.Print_Var(1,'123', 3)

# Print.Print_Global(100)

# # 变量测试
# Variable.VariableTest()
#
# # 运算符测试
# Math.MathTest()
#
# 循环测试
#LEOCycle.LEOCycleTest()

# 绘图测试
# Draw.DrawTest()

# log数据解析
# Log = LogProcess
# Log.LogProcess()

#Pyserial = Serial
#thread = Pyserial.Test()

# MultiProcess.Test()

# 算法学习
# classAlgorithm = Algorithm.Algorithm()


url='https://www.zhihu.com/question/22591304/followers'
#感觉这个话题下面美女多
headers={"美女"}
i=1
for x in range(20,3600,20):
    data = {'start':'0','offset':str(x),
          '_xsrf':'a128464ef225a69348cef94c38f4e428'}
    #知乎用offset控制加载的个数，每次响应加载20
    content = requests.post(url,headers=headers,data=data,timeout=10).text
    #用post提交form data
    imgs = re.findall('<img src=\\\\\"(.*?)_m.jpg',content)
    #在爬下来的json上用正则提取图片地址，去掉_m为大图
    for img1 in imgs:
        try:
            img1 = img.replace('\\','')
            #去掉\字符这个干扰成分
            pic=img1+'.jpg'
            path='d:\\bs4\\zhihu\\jpg\\'+str(i)+'.jpg'
            #声明存储地址及图片名称
            urllib3.urlretrieve(pic,path)
            #下载图片
            print ('下载了第'+str(i)+'张图片')
            i+=1
            sleep(random.uniform(0.5,1))
        #睡眠函数用于防止爬取过快被封IP
        except:
            print ('抓漏1张')
            pass
    sleep(random.uniform(0.5,1))

#myThread.threadTest()
print ("Good Bye 2017 & Welcome 2018")
#PygalDraw.DrawTest()
timeend = time.time() * MULTIPLE
print ("开始时间" + str(timestart))
print ("结束时间" + str(timeend))
print ("运行时间" + str(timeend - timestart))




if __name__ == "__main__":
    print ("主程序")

quit()