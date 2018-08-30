使用现成的博客模板修改
1 下载 copy index.html
    https://startbootstrap.com
    wget https://github.com/BlackrockDigital/startbootstrap-clean-blog/archive/gh-pages.zip
    解压
    index.html 放到 blog/templates/blog
    修改 views.py
        return render(request,'blog/index.html'
2 copy 素材
    把素材拷贝到项目里来
    项目根目录创建static文件夹
    在static 文件夹新建blog 文件夹
        mkdir static/blog -p
    css img js vendor 四个素材 copy 过去

3 修改配置文件
    my_blog/my_blog/settings.py
        最后添加
        #STATIC_URL = '/static'
        STATICFILE_DIRS = [os.path.join('static'),]
4 修改index.html

    找到所有css,js,图像
        修改链接，如下
        <link href="css/clean-blog.min.css" rel="stylesheet">
        修改为
        <link href="{% static 'blog/css/clean-blog.min.css' %}" rel="stylesheet">
        其他类似的都需要改

    开头的地方要加一行 载入静态文件
        #<!DOCTYPE html>
        #<html lang="en">
        {% load static %}

    标题改成模板写法
         <div class="post-preview">
            <a href="post.html">
              <h2 class="post-title">
                Man must explore, and this is exploration at its greatest
              </h2>
              <h3 class="post-subtitle">
                Problems look mighty small from 150 miles up
              </h3>
            </a>
            <p class="post-meta">Posted by
              <a href="#">Start Bootstrap</a>
              on September 24, 2018</p>
          </div>
          <hr>
        四个重复的去掉三个
        改成
            {% for post in post_list %}
             <div class="post-preview">
                <a href="post.html">
                  <h2 class="post-title">
                    {{post.title}}
                  </h2>
                  <h3 class="post-subtitle">
                    {{post.subtitle}}
                  </h3>
                </a>
                <p class="post-meta">Posted by
                  <a href="#">{{post.author}}</a>
                  {{post.date}}</p>
              </div>
              <hr>
              {% endfor %}

5 修改 blog/view.py
      def index(request):
          post_list = [
          {
            'link':'/blog/3/',
            'title':'第三篇博客！！！',
            'subtitle':'副标题',
            'author':'这是作者'，
            'date':'2018.3.25'
          },
          # *4
          ]
        flag = True

        return render(request,"blog/blog_index.html",
            {
                'title':'My blog title',
                'welcome':'welcome to my blog'
                'language_list':language_list,
                'link_dick':link_dick,
                'flag':flag,
                'post_list':post_list
            })
