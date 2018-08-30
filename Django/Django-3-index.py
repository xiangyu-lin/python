创建 app 默认首页

(pythonweb) [root@centos6 myblog]# mkdir blog/templates
(pythonweb) [root@centos6 myblog]# vim blog/templates/blog_index.html
# 随便写点内容 如index page

#修改 blog/views.py
(pythonweb) [root@centos6 myblog]# vim blog/views.py
    #def index(request):
        #return HttpResponse("welcome to My blog")
    #修改为-->
    def index(request):
        return render(request,"blog_index.html")
        # 在 render 中指定渲染某个模板 (blog_index.html)

Django会自动搜寻各个App的templates文件夹
然后在blog/templates/blog_index.html 中找到 并访问

---

问题 ：
不同app中可能存在同名的html文件,容易冲突?

解决方案
1.加前缀 比如 blog_index.html
2.在templates 文件夹中在建立和当前App同名的文件夹,html文件放到该文件夹中
    即原来是 blog/templates/blog_index.html
    改成 blog/templates/blog/index.html
    修改views.py 内容为：
    def index(request):
        return render(request,"/blog/index.html")
