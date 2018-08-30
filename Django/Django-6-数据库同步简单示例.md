## 数据库同步简单示例

**打开blog 应用里的models.py 文件**
```
(pythonweb)[root@xy pythonweb]# vim myblog/blog/models.py
```
```
from django.db import models

# Create your models here. #创建模型
class Post(models.Model): #添加一个post模型   继承
    title = models.CharField(max_length=80) #字符串 最大长度 80
```

**同步数据库**

1. 命令行运行python3 manage.py makemigrations
    > 会看到创建的模型(以及有没有错误提示)
```
(pythonweb) [root@xy myblog]# python3 manage.py makemigrations
```
```
Migrations for 'blog':
    blog/migrations/0001_initial.py
    - Create model Post
```

2. 继续运行 python3 manage.py migrate #（
    > 同步，迁移 得到如下提示  OK 同步完成
```
(pythonweb) [root@xy myblog]# python3 manage.py migrate
```
```
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

**修改blog文件夹里的admin.py**
> 利用admin 后台系统管理数据
```
(pythonweb) [root@xy myblog]# vim blog/admin.py
```
    from django.contrib import admin
    from .models import Post #当前文件夹models.py 导入
    # Register your models here.
    admin.site.register(Post)

修改models.py
>  __str__ 使 projetc(1) 就会变成标题名
```
(pythonweb) [root@centos6 myblog]# vim blog/models.py
```
```
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title
```
**访问 [http://192.168.112.61/admin/blog](http://192.168.112.61/admin/blog/)**
