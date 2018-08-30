#python3
#http://fcw06.com/ spider
#
import urllib.request
import urllib
import socket
import time
import re
import os
import sys

#https://jvrporn.com/videos/
#https://jvrporn.com/videos/page/6/

def listI(the_list): #取出列表中的字符串 前提是列表只有一项
    for i in the_list:
        the_list = i
        return(the_list)

def cD(path): # 切换一个目录 不存在则创建
    if os.path.exists(path):
        os.chdir(path)
    else:
        os.mkdir(path)
        os.chdir(path)

today =  time.strftime("%Y-%m-%d", time.localtime()) #获取年月日 2018-02-02

#进入保存文件的路径
try:
    os.chdir('E:\\')
except:
    pass

cD('O')
cD('other')
cD(today)


url = 'https://jvrporn.com/videos/page/8/'
html = urllib.request.urlopen(url).read().decode('utf-8') #获取网页并解码
# 获取视频所在网页地址列表

video_list = re.findall('href="(https://jvrporn.com/video/\d*/)"',html)
print(set(video_list))

for url in set(video_list):
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8') #获取视频地址html页面
        video_name = listI(re.findall('<h2>(.* )</h2>',html)) # 视频名字
        video_url = listI(re.findall('(https://.*\.mp4.*)" ',html)) #获取下载地址

        print('即将进入下载...')

        count1 = []
        def callbackfunc(blocknum, blocksize, totalsize):
            '''回调函数 获取下载进度
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



        if video_name == None:
            local = str(re.findall('(\d{5,10})',url)) + '.mp4'
        else:
            local = str(video_name).strip(':') + '.mp4'
        print(local)
        url = video_url
        #设置超时时间为30s
        socket.setdefaulttimeout(30)
        #解决下载不完全问题且避免陷入死循环
        try:
            urllib.request.urlretrieve(url,local,callbackfunc)
        except socket.timeout:
            count = 1
            while count <= 3:
                try:
                    urllib.request.urlretrieve(url,local,callbackfunc)
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                    print(err_info)
                    count += 1
            if count > 3:
                print("downloading " + local + " fialed!")
                saveLog("downloading " + local + " fialed!",'download.log')
                break

        print(video_name + 'Download success!')
        with open('download.log','a') as f:
            print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) + ' ' + video_name + ' ' + video_url + ' ' + ' Download success!',file=f)

    except Exception as err:
        try:
            print(str(err))
            with open('download.log','a') as f:
                print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) + ' ' + str(url) + ' ' + str(err),file=f)
        except:
            pass
