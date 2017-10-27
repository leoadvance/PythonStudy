#coding=utf-8
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import time
import os
import DeleteFile as df

# Create random data with numpy
import numpy as np

from datetime import datetime
# import pandas_datareader.data as web

def DrawTest():

    print ('\r\n绘图测试')
    print ('删除之前生成的html文件')
    # 删除之前建立的.html文件
    df.DeleteFile(os.path.abspath('.'), '.html')
    # 显示库版本
    print(plotly.__version__)
    # 设置认证信息
    plotly.tools.set_credentials_file(username='leoandlucky', api_key='gsyRblgkJatsjzInUOYf')
    #py.sign_in('leoandlucky', '2qdyfjyr7o')

    # 横坐标点数
    N = 100

    # 把0~N-1平均分成N份
    random_x = np.linspace(0, N - 1, N)

    # 生成正态分布随机数
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5

    print (random_x)
    print (random_y1)

    # Create traces
    trace0 = go.Scatter(
        x=random_x,
        y=random_y0,
        mode='markers',
        name='markers'
    )
    trace1 = go.Scatter(
        x=random_x,
        y=random_y1,
        mode='lines+markers',
        name='lines+markers'
    )
    trace2 = go.Scatter(
        x=random_x,
        y=random_y2,
        mode='lines',
        name='lines'
    )

    data = [trace0, trace1, trace2]
    FileName = "Plotly_Draw_" + "Random_" + time.strftime("%Y_%m_%d_%H_%M_%S",
                                                         time.localtime()) + ".html"
    print (FileName)
    #plotly.plotly.plot(data, filename=FileName)
    plotly.offline.plot(data, filename=FileName)

    return

# def Draw_Web():
#     df = web.DataReader("aapl", 'yahoo',
#                         datetime(2015, 1, 1),
#                         datetime(2016, 7, 1))
#
#     data = [go.Scatter(x=df.index, y=df.High)]
#     FileName = "Plotly_Draw_" + "Random_" + time.strftime("%Y_%m_%d_%H_%M_%S",
#                                                           time.localtime()) + ".html"
#     #py.iplot(data)
#     plotly.offline.iplot(data)