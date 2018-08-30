# python3
# upyun pic
import re
import os
import time
import urllib.request

#scp xcxc.html root@61,160.251.155:/var/www/html

html = urllib.request.urlopen('http://www.doer.ren/xcxc.html')
html = html.read().decode('utf-8')
url = re.findall('(photo.yupoo.com/xcxc789/[^"]*)" ta',html)

today =  time.strftime("%Y-%m-%d", time.localtime())
if os.path.exists(today):
    os.chdir(today)
else:
    os.mkdir(today)
    os.chdir(today)

for i in url:
    local = str(i[-8:]) + '.jpg'
    picurl = 'http://' + i
    urllib.request.urlretrieve(picurl,local)
    print(str(i) + ' save success...' )
    with open('upyunPicDownload.log','a') as f:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) + ' ' + str(i),file=f)
