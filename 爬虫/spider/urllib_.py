#python3 note
#urllib
#参考：
#   https://www.cnblogs.com/zhaof/p/6910871.html

# http://cn.python-requests.org/zh_CN/latest/

urllib.request #请求模块
urllib.error #异常处理模块
urllib.parse #url解析模块
urllib.robotparser #robots.txt解析模块

urlopen #适用于一些简单的请求  无法添加 header 等信息
    #urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
        import urllib.request
        response = urllib.request.urlopen('http://www.baidu.com')
        print(response.read().decode('utf-8'))

    urllib.requeset.urlopen(url,data,timeout) #一般常用的有三个参数，它的参数如下：
    response.read() #可以获取到网页的内容

    data #参数
    import urllib.parse
    import urllib.request
    data = byte(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
    print(data)
    response = urllib.request.urlopen('http://httpbin.org/post',data=data)
    print(response.read())

    timeout #参数 #设置超时时间
    import urllib.request
    try:
        response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
        print(response.read())
    except urllib.error.URLError as e:
        if isinstance(e.reason,socket.timeout): #import socket
            print('TIME OUT')

response
    response.status #获取状态码 没有()
    response.getcode() #同上
    response.reason #获取状态语句
    response.getheaders() #获取首部信息
    response.getheader("server") #获取指定 header
    response.read() #获得的是响应体的内容

request
    #添加请求头部信息
    import urllib.request
    req = urllib.request.Request('http://python.org')
    req.add_header('User-Agent','chrome')
    req.add_header('Host','www.baidu.com')
    response = urllib.request.urlopen(req)

    #定制头部信息
    from urllib import request,parse
    url = 'http://httpbin.org/post'
    headers = { #字典形式
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    dict = {
        'name':'zhangsan'
    }
    data = bytes(parse.urlencode(dict),encoding='utf8')
    req = request.Request(url=url,data=data,headers=headers,method='POST')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))

    #class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

#Handler
ProxyHandler #使用代理
    #步骤
    import urllib.request
    proxy_handler = urllib.request.ProxyHandler({ #创建一个代理 #参数是一个字典
    'http': '115.58.130.92:8118', #'代理类型' ：'地址：端口'
    'https': '115.58.130.92:8118'
    })

    opener = urllib.request.build_opener(proxy_handler) #创建一个opener

    #可选添加头部信息 注意addheaders = [('..','..')] 写的时候容易出错
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36')]
    #urllib.request.install_opener(opener) #可选安装opener
    #response = urllib.request.urlopen(url) #安装后可用普通 urlopen方式
    response = opener.open('http://httpbin.org/get') #调用opener
    printl(response.read())

    #代理ip可用性不高 考虑抓取列表随机使用
    # random.choise(iplist) #import random iplist = []
cookie,HTTPCookiProcessor
    #待办

urlparse #URL解析

    urlencode #方法 可以将字典转换为url参数
        from urllib.parse import urlencode
        params = {
            "name":"zhangsan",
            "age":23,
        }
        base_url = "http://www.baidu.com?"
        url = base_url+urlencode(params)
        print(url)
            #http://www.baidu.com?name=zhangsan&age=23

    urlparse #拆分url
        from urllib.parse import urlparse
        result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
        print(result)
            #ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5',fragment='comment')

    urlunparse #拼接url
        from urllib.parse import urlunparse
        data = ['http','www.baidu.com','index.html','user','a=123','commit']
        print(urlunparse(data))
            #http://www.baidu.com/index.html;user?a=123#commit

    urljoin #url拼接
        #拼接的时候后面的优先级高于前面的url

        from urllib.parse import urljoin

        print(urljoin('http://www.baidu.com', 'FAQ.html'))
            #http://www.baidu.com/FAQ.html
        print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
            #https://pythonsite.com/FAQ.html
        print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
            #https://pythonsite.com/FAQ.html
        print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
            #https://pythonsite.com/FAQ.html?question=2
        print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
            #https://pythonsite.com/index.php
        print(urljoin('http://www.baidu.com', '?category=2#comment'))
            #http://www.baidu.com?category=2#comment
        print(urljoin('www.baidu.com', '?category=2#comment'))
            #www.baidu.com?category=2#comment
        print(urljoin('www.baidu.com#comment', '?category=2'))
            #www.baidu.com?category=2

urlretrieve #直接将远程数据下载到本地
urllib.urlretrieve(url, filename, reporthook=None,data=None)
    url #外部或者本地url
    filename    #指定了保存到本地的路径如果未指定该参数，urllib会生成一个临时文件来保存数据
    reporthook  #是一个回调函数
    data    #指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)
                #  filename表示保存到本地的路径，header表示服务器的响应头。

    import urllib
    def callbackfunc(blocknum, blocksize, totalsize):
        '''''回调函数
        @blocknum: 已经下载的数据块
        @blocksize: 数据块的大小
        @totalsize: 远程文件的大小
        '''
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        print "%.2f%%"% percent

    url = 'http://www.sina.com.cn'
    local = 'd:\\sina.html'
    urllib.urlretrieve(url, local, callbackfunc)
