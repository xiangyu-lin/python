
#------
梳理 ：#处理过程 不包括数据库
    1.用户 http//192.168.112.52/blog/ -->
    2.myblog/myblog/urls.py  #网址解析
    #urlpatterns = [
        #path('admin/', admin.site.urls),
        path('blog/', include('blog.urls')), -->
    #]
    3.myblog/blog/urls.py
        #urlpatterns = [
            path('',views.index,name='blog_index'), --> #view.index 就是view.py 里面的index函数
            #path('<int:blog_id>',views.blog_detail,name='blog_detail')
        #]
    4.myblog/blog/views.py
        def index(request):
            return render(request,'blog/blog_index.html') -->
            把 blog/blog_index.html 渲染出来给用户
            #Django 会到 templates中找
