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

#选择
print('------------------------------------------------------------------------\
        \n以下任意类型可下载最新24部 \
        \n                 \
        \n有时源站网速会很慢,24个视频可能会下很久...\
        \n                 \
        \n默认下载到\"E:\O\other\当天日期"        \
        \n                 \
        \n选择下载的内容:   \
        \n                 \
        \n      1.国产自拍  \
        \n      2.韩国综合  \
        \n      3.日本有码  \
        \n      4.日本无码  \
        \n      5.成人动漫  \
        \n      6.偷拍系列  \
        \n      7.主页60部  \
        \n      0.退出程序  ')
print('-----------------------------------------------------------------------')
print()

user_input = input('输入喜欢的一项并回车：')

while int(user_input) not in range(8):
    user_input = input('请输入一个数字(0-7)：')

if user_input == '0':
    print('程序退出...')
    sys.exit()


choise = {
'1': 'http://www.fcw45.com/categories/27f8a5c9ce83cbfa7b70fc5c9a73a082/', #国产自拍
'2': 'http://www.fcw45.com/categories/bd2c9c41dffe88e87f713b64b60cc966/', #韩国综合
'3': 'http://www.fcw45.com/categories/c535ce35c36eb7fa67f39468157714f3/', #日本有码
'4': 'http://www.fcw45.com/categories/efc5f4716ea1e36b82dc5df866401ce7/', #日本无码
'5': 'http://www.fcw45.com/categories/46480850549e28993fb49cefcb75f82a/', #成人动漫
'6': 'http://www.fcw45.com/categories/df166ea541c4cbd16166c73feea36117/', #偷拍系列
'7': 'http://fcw45.com/'    #整页
}

url = choise[user_input] #根据用户输入选择 url
html = urllib.request.urlopen(url).read().decode('utf-8') #获取网页并解码

# 获取视频所在网页地址列表
video_list = re.findall('href="(http://www.fcw45.com/videos/.*/)',html)



for url in video_list:
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8') #获取视频地址html页面
        video_name = listI(re.findall('"og:title" content="(.*)"',html)) # 视频名字
        video_url = listI(re.findall('(http://.*\.mp4)/\?',html)) #获取下载地址
        print(video_url)
        """
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

        url = video_url
        local = video_name + '.mp4'

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
        """
    except Exception as err:
        print(str(err))
        with open('download.log','a') as f:
            print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) + ' ' + url + ' ' + str(err),file=f)
