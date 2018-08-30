设计简易版博文模型
  Django 中可用的各类模型 此处只用这三种
      CharField #普通字串  如姓名 标题等 短一点
      DateTime #日期格式
      TextField #大段的文章

  博客相关信息有如下
      1.标题 CharField
      2.副标题 CharField
      3.作者 CharField
      4.发表日期 DateTimeField
      5.标签 CharField
      6.分类 CharField
      7.博文内容 TextField
      8.博文链接 CharField
      9.（可选）点赞数 IntegerField
      10.（可选）阅读量 IntegerField

  作者 标签 分类 每张表都存会产生大量重复所以
      3.作者 CharField 关联作者模型  作者模型（Django自带）
      5.标签 CharField 关联标签模型
      6.分类 CharField 关联分类模型  分类模型 （内容：分类名称1,.. 选用模型：CharField）


  models.py

      博文基础模型
      # Create your models here.
      class Post(models.Model):
          title = models.CharField(max_length=80) #可用 default='' 参数设置默认值
          subtitile = models.CharField(max_length=80)
          publish_date = models.DateTimeField() #发表日期
          content = models.TextField()
          link = models.CharField(max_length=100)

      关联作者模型 #models.py 开头处导入作者模型
      from django.contrib.auth.models import User

          #link = models.CharField(man_length=100)
          author = models.ForeignKey(User,on_delete=models.CASCADE)
              #用 ForeignKey 关联另一个模型  #两个参数都要填

      新建分类模型和标签模型
      添加两个class
      #from django.contrib.auth.models import User
      class Category(models.Model):
          name = models.CharField(max_length=100)
          def __str__(self):
              return self.name
      class Tags(models.Model):
          name = models.CharField(max_length=100)
          def __str__(self):
              return self.name
      class Post(models.Model):

      关联分类模型
      class Post(models.Model):
          title = models.CharField(max_length=80)
          subtitle = models.CharField(Max_length=80)
          publish_date = models.DateTimeField() #发表日期
          content = models.TextField()
          link = models.CharField(max_length=100)
          author = models.ForeignKey(User,on_delete=models.CASCADE)
          Category = models.ForeignKey(Category,on_delete=models.CASCADE)
          Tags = models.ManyToManyField(Tags,blank=True) #允许为空

      利用 ManyToManyField() 也可关联另外一个模型
      ForeignKey 和 ManyToManyField 区别在哪
          一对多关系 用 ForeignKey  #一篇文章只有一个分类 一个分类下会有多个文章
          多对多关系 用 ManyToManyField 如文章对标签

      每次修改模型都要同步数据库
          python3 manage.py makemigrations

          同步时如果添加字段之前有数据
          会让你为 不能为空的字段 添加值 一般打个1就行
              日期可以用 timezone.now

          python3 manage.py migrate

          不行就把数据库删了 直接按照现在模型重新创建 没什么数据的情况下

admin.py

    from django.contrib import admin
    from .models import Post,Tags,Category #记得要导入
    # Register your models here.
    admin.site.register(Post)
    admin.site.register(Tags)
    admin.site.register(Category)

----------------

数据库中提取真正的博文信息
