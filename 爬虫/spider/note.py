urllib #模块
    urllib.request
    urllib.request.urlopen(url,data,head) #date赋值就是post方式 #head 是字典形式

    urllib.parse.quote(content) #空格转换成%20  #也可以处理包含中文的url

    decode('utf-8') utf8解码成 unicode

    import time
    time.sleep(5)
    print('1')

请求一个网页并显示
    import urllib.request #导入urllib.request模块
    response = urllib.request.urlopen("http://www.doer.ren/devinit.sh")
        #urllib.request.urlopen() 方法请求一个url
    html = response.read() # read() 方法读取对象
    html = html.decode('utf-8') #解码
    print(html)

下载一个图片
    import urllib.request
    response = urllib.request.urlopen('http://placekitten.com/g/500/600')
    cat_image = response.read()
    with open('E:\Python\爬虫\cat.jpg','wb') as f: #打开文件写入模式二进制
        f.write(cat_image) #保存

抓取google翻译结果
    #pythonFIle\mine\translation.py
