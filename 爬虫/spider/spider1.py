#python3 test
import urllib.request
import urllib.error
import socket
import os
import requests
import sys
import json
import re
from printl import printL

def getUrl(url,header={},proxy=None,cookie=None,timeout=None,data=None):
    '''A simple getUrl function.

    5 agrument:url,header=None,,proxy=None,cookie=None,timeout=None
        url             url,
        header=None     add header, example: header={'User-Agent':'chrome'}
        proxy=None      add prxoy,
        cookie=None     set cookie,
        timeout=None    timeout,
        data=None       POST request.
    '''
    global response
    if proxy != None:
        print('This argument useless yet!')
    elif cookie != None:
        print('This argument useless yet!')

    else:
        req = urllib.request.Request(url,data=None,headers=header)
        try:
            response = urllib.request.urlopen(req,timeout)
        except urllib.error.HTTPError as e:
            print('\nHTTP Error : ' + '\t' + str(e.code) + ' ' + str(e.reason))
            print()
            sys.exit()

        except urllib.error.URLError as e:
            if isinstance(e.reason,socket.timeout): #import socket
                print('TIME OUT')
            else:
                print('URLError' + str(e.reason))
            sys.exit()
        else:
            pass
    return(response)

<div class="flot-tick-label tickLabel" style="position: absolute; top: 2px; left: 0px; text-align: right;">250</div>

#html = getUrl('http://uplog.s.upyun.com/logstash-vista_403_access_error-2018.02.07/_search?search_type=count',header={'Cookie':'_ga=GA1.2.410581199.1517732476; Hm_lvt_09e47f90c12c9a15516512c0d87f6791=1517732476,1517732480; _oauth2_proxy=eWRfbW9uaXRvckB1cGFpLmNvbQ==|1517989853|EBqomqYqv32GTmI7L72HVxjc8e0=','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'})
#html = getUrl('https://cdn-node-status.s.upyun.com/node-stats.html',header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36','Referer':'https://cdn-node-status.s.upyun.com/node-stats.html'})

while True:
    tooks = []
    while True:
        #html = getUrl('http://uplog.s.upyun.com/logstash-vista_403_access_error-2018.02.07/_search?search_type=count',header={'Cookie':'_ga=GA1.2.410581199.1517732476; Hm_lvt_09e47f90c12c9a15516512c0d87f6791=1517732476,1517732480; _oauth2_proxy=eWRfbW9uaXRvckB1cGFpLmNvbQ==|1517989853|EBqomqYqv32GTmI7L72HVxjc8e0=','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'})
        html = getUrl('http://uplog.s.upyun.com/logstash-marco_access_error-2018.02.07/_search',header={'Cookie':'_ga=GA1.2.410581199.1517732476; Hm_lvt_09e47f90c12c9a15516512c0d87f6791=1517732476,1517732480; _oauth2_proxy=eWRfbW9uaXRvckB1cGFpLmNvbQ==|1517989853|EBqomqYqv32GTmI7L72HVxjc8e0=','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'})


        for i in (re.findall(':(\d*) ',html.getheader('Date'))):
            time = i
        if time != 30 or time != 00:
            for i in re.findall('took":(\d*),',html.read().decode('utf-8')):
                tooks.append(i)
                print(i)
        else:
            print(html.getheader('Date'))
            break
    print(sum(tooks))
    break
"""
html = getUrl('http://uplog.s.upyun.com/logstash-marco_access_error-2018.02.07/_search',header={'Cookie':'_ga=GA1.2.410581199.1517732476; Hm_lvt_09e47f90c12c9a15516512c0d87f6791=1517732476,1517732480; _oauth2_proxy=eWRfbW9uaXRvckB1cGFpLmNvbQ==|1517989853|EBqomqYqv32GTmI7L72HVxjc8e0=','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'})

for i in (re.findall(':(\d*) ',html.getheader('Date'))):
    time = i
    print(time)
for i in re.findall('took":(\d*),',html.read().decode('utf-8')):
    print(i)
"""
"""
#print(json.load(html))





def downLoad(url,l_file='localfile',path='E:\\Download',proxy=None,header=None):
    '''A simple downLoad url.

    argument: url,l_file=localfile,path='E:\\Download',header=None
            example header=('User-Agent','chrome')

    '''
    try:
        os.chdir(path)
    except:
        os.chdir('E:\\')
    if proxy != None or header != None:
        #proxy_handler = urllib.request.ProxyHandler({ #创建一个代理 #参数是一个字典
        #'http': '115.58.130.92:8118', #'代理类型' ：'地址：端口'
        #'https': '115.58.130.92:8118'
        #})
        opener=urllib.request.build_opener()#proxy_handler)
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, l_file)

try:
    downLoad('http://jandan.net/ooxx',l_file='jiandan.html')#,header=('User-Agent','chrome'))
except urllib.error.HTTPError as e:
    print(str(e) + '\n\n请使用header 或者 proxy 参数'
"""
