#python3
#fuliba.net pic

#http://fuliba.net/
#http://fuliba.net/page/2
#http://fuliba.net/page/3

import urllib.request #导入模块
import os
import time

image_list = [] #存放图片url
page_list = [] #存放index 包含的子页面
today =  time.strftime("%Y-%m-%d", time.localtime()) #获取日期 2018-2-4

def cdToday(folder=today):
    if os.path.exists(folder):
        os.chdir(folder)
    else:
        os.mkdir(folder)
        os.chdir(folder)

def getUrl(url): #请求一个url，不解码
    req = urllib.request.Request(url) #生成一个对象请求
    #这个对象中加 header
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36')
    request = urllib.request.urlopen(req) #请求这个对象内容返回给 request
    html = request.read() #读取结果赋值给 html
    return(html) #返回html

def findList(index1,index2,a_step,b_step,save_list):
    '''定义函数查找需要的url.

    五个参数，前两个是查找的字串，step是取值用的，表示从查找的字符位置前后移动几个字符
    方便取到需要的内容.save_list保存结果.    
    '''
    a = html.find(index1)
    while a != -1:
        b = html.find(index2,a,a+100)
        if b != -1:
            save_list.append(html[a+a_step:b+b_step])
        else:
            b = a + 9
        a = html.find(index1,b)
    return(save_list)

def getPagelist(index_page='http://fuliba.net'):
    global page_list
    global html
    html = getUrl(index_page).decode('utf-8') #请求主页 并解码
    findList('fuliba.net/','.html',-7,5,page_list)
    page_list = list(set(page_list))
    return(page_list)

def downLoadImg(the_list=image_list):
    for i in the_list:
        try:
            filename = i.split('/')[-1]
            img = getUrl(i)
            if len(img) < 50000: #过滤掉 50k以下的
                continue
            with open(filename,'wb') as f:
                f.write(img)
                print(str(i) + '    save Success!')
        except:
            pass


index = 'http://fuliba.net/page/6'
getPagelist() #获取文章列表page_list

os.chdir('E:\Python\爬虫')
cdToday(today)
#printl(sort_page_list)

for i in page_list:
    image_list = []
    printl(image_list)
    global html
    #获取url列表
    html = getUrl(i).decode('utf-8')
    findList('src=','.jpg',5,4,image_list)
    findList('src=','.gif',5,4,image_list)
    file_dir = str(i.split('.')[-2].split('/')[-1])
    cdToday(file_dir)
    downLoadImg(image_list)
    os.chdir('../')
