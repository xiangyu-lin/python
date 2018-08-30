#python3
#
from spider import getUrl
from printl import printL
import urllib.request
import urllib
import socket
import time
import re
import os

def listI(the_list): #取出列表中的字符串 前提是列表只有一项
    '''the_list = listI(the_list).
    '''
    for i in the_list:
        the_list = i
        return(the_list)

os.chdir('E:\O\other') #进入保存文件的路径
today =  time.strftime("%Y-%m-%d", time.localtime()) #获取年月日 2018-02-02
# 进入以今天命名的文件夹 没有则创建
if os.path.exists(today):
    os.chdir(today)
else:
    os.mkdir(today)
    os.chdir(today)

#http://fcw06.com/  #主页
# <meta property="og:title" content="122314_944-1pon-親友の彼女 椎名みゆ">

url = 'http://fcw06.com/'
html = getUrl(url)
html = html.read().decode('utf-8')

# 获取视频所在网页地址列表
video_list1 = re.findall('href="(http://www.fcw06.com/videos/.*/")',html)
video_list = []
for i in video_list1:
    video_list.append(i.strip('"'))
with open('spiderFeicai.log','a') as f:
    print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))),file=f)
    print('本次共抓取 ' + str(len(video_list)) + ' 个视频地址.')
    with open('spiderFeicai.log','a') as ff:
        printL(video_list,f=ff)

for url in video_list:
    try:
        html = getUrl(url).read().decode('utf-8') #获取视频地址html页面
        Isvip = re.findall('仅限会员观看',html)

        video_name = re.findall('"og:title" content="(.*)"',html) # 视频名字
        video_name = listI(video_name)
        video_url = re.findall('(http://.*\.mp4)/\?',html) #获取下载地址 是个列表
        video_url = listI(video_url) #视频地址转换成字符串

        if '仅限会员观看' not in Isvip: #判断是否会员 #并保存日志
            print('非仅会员视频，忽略')
            with open('notVip.log','a') as f:
                print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) + '\n' + video_name + '\n' + video_url,file=f)
            break
        else:
            print('会员视频，即将进入下载...')
            with open('Vip.log','a') as f:
                print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) + '\n' + video_name + '\n' + video_url,file=f)
        #video_size = re.findall('MP4, (.*) Mb',html) #MP4 大小
        #video_size = int(float(listI(video_size))): #取出列表中的字符串 变成整数
        # 回调函数 获取下载进度
        count1 = []
        def callbackfunc(blocknum, blocksize, totalsize):
            '''回调函数
            @blocknum: 已经下载的数据块
            @blocksize: 数据块的大小
            @totalsize: 远程文件的大小
            '''
            percent = 100.0 * blocknum * blocksize / totalsize
            if percent > 100:
                percent = 100
            count = str((percent))[:3]
            if not count in count1:
                print("%.1f%%"% percent + '    ' +   local)
            count1.append(count)

        url=video_url
        local = video_name

        #设置超时时间为30s
        socket.setdefaulttimeout(30)
        #解决下载不完全问题且避免陷入死循环
        try:
            urllib.request.urlretrieve(url,local,callbackfunc)
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(url,local,callbackfunc)
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading " + local + " fialed!")
                with open('Vip.log','a') as f:
                    print("downloading " + local + " fialed!",file=f)

        #urllib.request.urlretrieve(url,local,callbackfunc)
    except Exception as err:
        print(str(err))
