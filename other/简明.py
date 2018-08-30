废弃...

chapter 4 基本概念
    Python 有4种类型的数
        整数、长整数、浮点数、复数（-5+4j）
    字符串 #单双或三引号引起来
        字符串不可变

        自然字符串
            例如 r"Newlines are indicated by \n"
        Unicode 字符串
            例如 u"This is a Unicode string."
        按字面意义级连字符串
            print('what is your' +  ' name')
            ==>print('what is your' ' name')
    变量
    标识符(变量)的命名 #标识符是变量的例子
        大小写字母或下划线开头
        其他部分可以用大小写或数字下划线
        区分大小写
    逻辑行与物理行
        '\' #反斜线表示不换行 #使用括号时也暗示不换行


    range(1,100,25) #1-100 步长25 不包括100
    s = raw_input('Enter something:') #读入数据赋值给s
    break # 退出循环

chapter 7 #函数
    def fname(arg): 定义函数
        pass

    global x,y,z   #定义全局变量x,y,z 即在函数外也生效
    def func(a,b=0) #默认参数
    return x    #return跳出函数 也可返回x值
    pass
    DocStrings #第一个逻辑行的文档字符串
        首行大写字母开始句号结尾
              #第二行是空行
              #第三行是具体描述
              def printMax(x,y):
                  '''Print the maximum of two numbers.

                  the two num must be int'''
                  x = int(x) #convert to integers,if possible
                  y = int(y)
                  if x > y:
                      print x,'is max!'
                  else:
                      print y,'is maximum!'

              printMax(3,5)
              print printMax.__doc__

chapter 8 #模块
    import sys #导入模块
    sys.argv #包含了命令行参数列表；即命令行传递的参数  argv变量
    print 'The command line argument are:'
    for i in sys.argv:
        print i

    print '\n \nThe Python PATH is :',sys.path,'\n' #sys.path 包含输入模块的目录名列表

    from sys import argv  #尽量不用
    模块的 __name__
    if __name__ == '__main__':
        print 'This program is being run by itself'
    else:
        print 'I am being imported from another modules'
    制造模块
        #!/bin/python
        #Filename:mymodule.py
        def sayhi():
            print 'Hi,this is mymodule speaking.'
        version = '0.1'
        #End of mymodule.py

        >>> import mymodule
        >>> mymodule.sayhi()
        Hi,this is my modules speaking.
        >>> print 'version',mymodule.version
        version 0.1

    dir(sys)
        dir() #返回当前模块的属性列表
        del a #删除一个变量

chapter 9 #数据结构
    列表
        #This is my shopping list
        shoplist = ['apple','mango','carrot','banana']
        print 'I have',len(shoplist),'items to purchase.'
        print 'These items are:',
        for i in shoplist:
            print i
        print '\n I also have to buy rice.'
        shoplist.append('rice')
        print 'My shoplist is now:',shoplist

        print 'I will sort my list now\n'
        shoplist.sorted()
        print 'Sorted shoplist is:',shoplist

        print 'the first item i will buy is',shoplist[0]
        olditem = shoplist[0]
        del shoplist[0]
        print 'I bought the',olditem
        print 'My shoplist is now',shoplist
        元组
        zoo = ('wolf','elephant','penguin')
        print 'Number of animals in the zoo is',len(zoo)

        new_zoo = ('mokey','dolphin',zoo)
        print 'Number of in new_zoo is',len(new_zoo)
        print 'All animals in new_zoo are',new_zoo
        print 'animals brought from old are',new_zoo[2]
        print 'Last animals brought from old zoo is',new_zoo[2][2]

        age = '22.3s'
        name = 'Swaroop'
        print '%s is %d years old' % (name,float(age)) #%s字符串 %d整数

        字典
        #'ab' is short for 'a'ddress'b'ook
        ab = {  'Swaroop'   :   'Swaroopch@qq.com',
                'Larry'     :   'Larry@qq.com'
                'Matsumoto' :   'Matsumoto@163.com'
                'goldendog' :   'goldendog@qq.com'
             }
        print "Swaroop's address is %s" %s ab['Swaroop']
        #Adding a key/value pair
        ab['beigou'] = 'guido@python.org'
        #delete a key/value pair
        del ab['goldendog']

        print '\nThere are %d contactd in the address-book\n' % len(ab)
        for name,address in ab.items(): #字典的items方法
            print 'contact %s at %s' % (name,address)
        if 'guido' in ab: # OR ab.has_key('guido')  #dict has_key方法
            print "\nguido's address is %s" % ab['guido']

        序列 #列表元组字符串都是序列
            shoplist = ['apple','mango','carrot','banana']

            #indexing or 'Subscription' opreation
            print 'Item 0 is',shoplist[0]
            print 'Item 1 is',shoplist[1]
            print 'Item 2 is',shoplist[2]
            print 'Item 3 is',shoplist[3]
            print 'Item -1 is',shoplist[-1] #倒数第一
            print 'Item -2 is',shoplist[-2] #倒数第二

            #Slicing on a list
            print 'Item 1 to 3 is',shoplist[1:3]
            print 'Item 2 to end',shoplist[2:]
            print 'Item 1 to -1 is',shoplist[1:-1]
            print 'Item start to end is',shoplist[:]

            #Slicing on a string
            name = 'Swaroop'
            print 'characters 1 to 3 is',name[1:3]
            print 'characters 2 to end is',name[2:]
            print 'characters 1 to -1 is'name[1:-1]
            print 'characters start to end is',name[:]
         字符串方法
            name = 'Swaroop'  #this is a string object
            if name.startswith('Swa'): #startswith方法 测试字符串是否以给定字符串开头
                print 'Yes,the string startswith "Swa"'
            if a in name: #in操作符 检测是否为另一个字符串的一部分
                print 'yes,is contains the string "a"'
            if name.find('war') != -1:
                print 'yes,it contains the string "war"'
            delimiter = '_*_'
            mylist = ['Brazil','Russia','India','China']
            print delimiter.join(mylist) #jion方法替换分隔符

chapter 10
        #!/bin/python backup v1
        import os #导入模块
        import time
        #1.The files and directories to be backed up are specified in a list.
        source = ['/tmp/swaroop/','/home/xylin/working/']
        #2.The backup must be stored in a mian backup directory.
        target_dir = '/tmp/backup/backup' #remember to change this to want you will be using
        #3.The files are backup into a zip file.
        #4.The name of the zip archive is the current data and time
        target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip' #time.strftime()函数获取时间
        #5.We use the zip command (in Unix/linux) to put the file in a zip archive
        zip_command = "zip -qr '%s' %s" % (target,' '.join(source)) #jion方法把列表转换成字符串
        #run backup
        if os.system(zip_command) == 0:
            print 'Successful backup to',target
        else:
            print 'backup failed'

        #!/bin/python backup v2
        import os
        import time
        #1.The files and directories to be backed up are specified in a list.
        source = ['/tmp/swaroop/','/home/xylin/working/']
        #2.The backup must be stored in a mian backup directory.
        target_dir = '/tmp/backup/' + time.strftime('%Y%m%d')  #remember to change this to want you will be using
        #3.The files are backup into a zip file.
        #4.The name of the zip archive is the current data and time
        target = target_dir + os.sep + time.strftime('%H%M%S') + '.zip' #os.sep 根据操作系统给出目录分隔符
        #5.We use the zip command (in Unix/linux) to put the file in a zip archive
        zip_command = "zip -qr '%s' %s" % (target,' '.join(source))
        #run backup
        if not os.path.exists(target_dir):
           os.mkdir(target_dir) #make directory
           print 'Successfully created directory',target_dir
        if os.system(zip_command) == 0:
           print 'Successful backup to',target
        else:
           print 'backup failed'

        #!/bin/python backup v3
        import os
        import time
        #1.The files and directories to be backed up are specified in a list.
        source = ['/tmp/swaroop/','/home/xylin/working/']
        #2.The backup must be stored in a mian backup directory.
        note = raw_input('give update some note:')
        target_dir = '/tmp/backup/' + time.strftime('%Y%m%d')   #remember to change this to want you will be using
        #3.The files are backup into a zip file.
        #4.The name of the zip archive is the current data and time
        target = target_dir + os.sep + time.strftime('%H%M%S') + note + '.zip'
        #5.We use the zip command (in Unix/linux) to put the file in a zip archive
        zip_command = "zip -qr '%s' %s" % (target,' '.join(source))
        #run backup
        if not os.path.exists(target_dir):
            os.mkdir(target_dir) #make directory
            print 'Successfully created directory',target_dir
        if os.system(zip_command) == 0:
            print 'Successful backup to',target
        else:
            print 'backup failed'

chapter 11 #面向对象的编程

        #
        class Person:
            '''Represents a Person.'''
            population = 0

            def __init__(self,name):
                '''Initializes the person's data.'''
                self.name = name
                print '(Initializes %s)' % self.name
                #when this persion is created,he/she
                #adds to the population
                Person.population += 1

            def __del__(self):
                '''I am dying.'''
                print '%s says bye' %self.name
                Person.population -= 1
                if Person.population == 0:
                    print 'I am the last one.'
                else:
                    print 'There are still %d people left.',Person.population

            def sayhi(self):
                '''Greeting by the persion.

                really,that's all it does.'''
                print 'Hi my name is %s.' % self.name

            def howmany(self):
                '''print the current population.'''
                if Person.population == 1:
                    print 'I am the only person here.'
                else:
                    print 'We have %d persons here.' % Person.population

        Swaroop = Person('Swaroop')
        Swaroop.sayhi()
        Swaroop.howmany()

        kalam = Person('Abdul kalam')
        kalam.sayhi()
        kalam.howmany()

        Swaroop.sayhi()
        Swaroop.howmany()

        #继承
