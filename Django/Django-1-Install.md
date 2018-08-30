**.                           
Django 基础                                                                                                 .**

> 创建虚拟环境并在里面安装 django
> Atom下阅读

# [root@centos6 ~]# mkdir pythonweb
# [root@centos6 ~]# cd pythonweb/
> 创建项目目录进入

# [root@centos6 pythonweb]# python3 -m venv ./  
> 创建虚拟环境当前目录
  用虚拟环境装django 不影响其他django项目 但系统的 Django 可能影响虚拟环境里的

# [root@centos6 pythonweb]# source bin/activate
> (pythonweb) [root@centos6 pythonweb]#
  激活虚拟环境  出现括号

    --- 以下在虚拟环境中运行 ---

# (pythonweb) [root@centos6 pythonweb]# pip3 install django
> 安装Django

# (pythonweb) [root@centos6 pythonweb]# django-admin startproject myblog
> 创建项目 myblog
  my_blog 是网站项目名 不要用Django 或者test 之类容易产生冲突的名称

# (pythonweb) [root@centos6 pythonweb]# vim myblog/myblog/settings.py
> 编辑配置文件 允许 本机 ip 192.168.112.53 作为服务器
  #最后一行添加

  ALLOWED_HOSTS = ['192.168.112.52', 'localhost', '127.0.0.1']

# (pythonweb) [root@centos6 pythonweb]# cd myblog/
# (pythonweb) [root@centos6 myblog]# python3 manage.py runserver 192.168.112.52:80
> 运行 django 在本机ip 192.168.112.52 的 80端口

# (pythonweb) [root@centos6 ~]# deactivate
> [root@centos6 ~]#
  退出虚拟环境 括号没了

---

> 创建管理员账号
# (pythonweb) [root@centos6 myblog]# python3 manage.py createsuperuser
>Username (leave blank to use 'root'): admin
Email address: xiangyu.lin@verycloud.cn
Password: admin123
Password (again): admin123
Superuser created successfully.

> 访问
http://192.168.112.52/admin

---

### 遇到的问题

  1. 安装Django
      pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.

      yum -y install openssl-devel
      cd Python..
      make && make install

  2. django-admin startproject my_blog
      -bash: django-admin: command not found

      ln -sv /user/local/python3/bin/django-admin /usr/bin/django-admin

  3. python3 manage.py runserver 192.168.112.52:80
      `from _sqlite3 import *`
      ModuleNotFoundError: No module named '_sqlite3'`

      yum -y install sqlite-devel
      cd Python
      make && makeinstall
