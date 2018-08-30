模板

1. 渲染
    vim myblog/blog/templates/blog/index.html  两个花括号
        <h1>{{title}}</h1>
        <p>{{welcome}}</p>

    vim blog/view.py
        def index(request):
            return render(request,"blog/blog_index.html",
                {
                    'title':'My blog title', #
                    'welcome':'welcome to my blog'
                })

2. 渲染列表
    vim myblog/blog/templates/blog/index.html
        <ul>
        {% for i in language %} #百分号+花括号 表示是模板语句
            <li>{{i}}</li>
            #<li>{{forloop.counter}}.{{i}}</li>                         #. 自己加的 效果 1.python 2.
        {% endfor %}    #此处要添加 endfor 声明结束
        </ul>

    #{{forloop.counter}} for 循环中的计数 从1开始
    #forloop.counter0 如果需要从零开始

    vim blog/view.py
        language_list = ['Python','C++','Java']
        #def index(request):
            #return render(request,"blog/blog_index.html",
                #{
                    #'title':'My blog title',
                    #'welcome':'welcome to my blog'
                    'language_list':language_list
                #})

3 渲染字典
    vim blog/view.py
        #def index(request):
            linkdict = {'doerren':'http://www.doer.ren','baidu':'http://www.baidu.com'}
            #return render(request,"blog/blog_index.html",
                #{
                    #'title':'My blog title',
                    #'welcome':'welcome to my blog'
                    #'language_list':language_list,
                    'link_dict':linkdict
                #})

    blog_index.html
        <a class="link" href="{{link_dick.doerren}}">DOer.ren</a>
        <a class="link" href="{{link_dick.baidu}}">BAidu.com</a>

4 模板中的条件判断
blog/view.py
    添加一个 flag 设置为 True
    #def index(request):
        #link_dict = {'doerren':'http://www.doer.ren','baidu':'http://www.baidu.com'}
        flag = True

        #return render(request,"blog/blog_index.html",
            #{
                #'title':'My blog title',
                #'welcome':'welcome to my blog'
                #'language_list':language_list,
                #'link_dict':link_dict,
                'flag':flag
            #})

blog_index.html
    {% if flag %}
        <p id="welcome-line">欢迎1...</p>
    {% else %}
        <p id="welcome-line">欢迎2...</p>
    {% endif %}

    最后别忘记 endif
    elif else and or 等关键词都可以使用

5 判断用户是否登录
    vim blog/templates/blog/index.html
    {% if request.user.is_authenticated %}
        <p>{{request.user.username}},welcome...</p>
    {% else %}
        <p>Please login...</p>
    {% endif %}
