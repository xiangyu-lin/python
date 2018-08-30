Django APP views.py & urls.py
#视图和网址

1. #blog 为 app名 创建 blog app
(pythonweb) [root@centos6 myblog]# python3 manage.py startapp blog

2. # 编辑配置文件 INSTALLED_APPS 添加blog
(pythonweb) [root@centos6 myblog]# vim myblog/settings.py

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    ]
        # ↑ 此处添加blog

3. #编辑视图 view
(pythonweb) [root@centos6 myblog]# vim blog/views.py

    from django.shortcuts import render
    from django.http import HttpResponse #引入 HttpResponse 函数

    # Create your views here.
    def index(request):  #定义index函数 处理主页访问请求
        return HttpResponse("welcome to My blog") #用response 返回给用户

4. # 创建urls.py   用于处理网址解析
(pythonweb) [root@centos6 myblog]# vim blog/urls.py
    # 填入以下内容
    from django.urls import path
    from . import views #从当前文件夹（模块）引进

    urlpatterns = [
        path('',views.index,name='blog_index'), #访问的 url给 views.index来处理
    ]

5. # 配置项目的 urls.py
(pythonweb) [root@centos6 myblog]# vim myblog/urls.py
    # 修改 myblog 文件夹里的urls.py
    # 添加两处内容 include 和 path

    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls')),
    ]

#访问 http://191.168.112.61/blog
---

6. # 附 更复杂的网址处理

#编辑 urls.py 添加 path('<int:blog_id>',views.blog_detail,name='blog_detail')
(pythonweb) [root@centos6 myblog]# vim blog/urls.py
    from django.urls import path
    from . import views #从当前文件夹（模块）引进
    urlpatterns = [
        path('',views.index,name='blog_index'), #访问的 url给 views.index来处理
        path('<int:blog_id>',views.blog_detail,name='blog_detail')
        #数字提取出来 放到views.blog_detail 处理
        #<int:blog_id> 表示这个网址是个数字 存到blog_id 这个变量里
    ]
#编辑 views.py
(pythonweb) [root@centos6 myblog]# vim views.py
    def blog_detail(request,blog_id):
        return HttpResponse(blog_id) #直接返回 blog_id

#访问 http://192.168.112.61/blog/10     #10 可以为任意数字
