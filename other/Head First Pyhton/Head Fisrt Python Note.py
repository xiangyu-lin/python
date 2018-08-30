#!/Bin/python
#
第一章 初识pyhton #人人都爱列表
    movies = ["The Holy Grail","The Life of Brain","The meaning of life"] #创建列表
    print(movies[1]) #print() BIF 打印列表第二项
    len(movies) #列表长度  len() BIF
    movies.append("The Shawshank Redemption") #append()方法 在末尾增加数据项
    movies.extend("film","another film") #extend方法 #末尾增加数据集
    movies.pop() #pop()方法 从末尾删除数据
    movies.remove("The Holy Grail") #remove()方法  #删除某项数据
    movies.insert(1,"1975") #insert()方法插入数据在[1]处
    print(movies[4][1][3]) #打印嵌套列表中的嵌套

    count=0                    #"while"-- print each_item of list
    while count < len(movies):
        print(movies[count])
        count=count+1
    #for better than whlie

    isinstance() #BIF 检查某个特定标识符是否包含某个特定类型的数据

    for each_item in movies:    #处理一个内嵌列表
        if isinstance(each_item,list):    #if each_item is list
            for i in each_item:
                print(i)
        else:
            print(each_item)

    #创建一个函数
    def printl(the_list):
        for i in the_list:
            if isinstance(i,list):
                printl(i)
            else:
                print(i)

    toolz:
        print() #BIF 打印到屏幕
        len() #BIF 提供某个数据对象的长度
        isinstance() #BIF 检查某个特定标识符是否包含某个特定类型的数据
        def # 定义函数

第二章 共享你的代码 #函数模块

    #发布准备
    nester.py
    setup.py
    '''
    from distutils.core import setup  #从python发布工具导入setup函数

    setup(
            name        = 'nester',
            version     = '1.0.0',
            py_modules  = ['nester'], #将模块元数据与setup函数关联
            author      = 'hfpython',
            author_email= 'xiangyu.lin@verycloud.cn',
            url         = 'http://www.doer.ren',
            description = 'A simple printer of nested list',
        )
    '''
    #构建发布文件
    python3 setup.py sdist
    #install
    sudo python3 setup.py install

    nester
        MANIFEST # 这个文件包含发布中的文件列表
        build
            lib #代码在这个文件中
        dist
            nester-1.0.0.tar.gz #这是发布包
        nester.py #代码
        nester.pyc #'编译'版本的代码
        setup.py #元数据

    #使用 import
    import nester
    nester.printl(list) #模块名.函数

    PYPI
        xiangyu.lin
        xiangyu.lin@power
        3139303033@qq.com

    #windows
    pip install -U pip setuptools twine
    twine upload dist/*

    #下载指定版本
    pip install printlin==1.1.0

    #range() BIF
    range() 返回一个迭代器，根据需要生成一个指定范围的数字
        #生成直到4但不包括4的数字 0123
        for i in num(4)
            print(i)

    #nester
    def printl(the_list,indent=False,level=0):
        for i in the_list:
            if isinstance(i,list):
                printl(i,indent,level+1)
            else:
                if indent:
                    for tab_stop in range(level):
                        print("\t",end='')
                print(i)

    #BIF
    list()          这是一个工厂函数，创建一个新的空列表
    enumerate()     创建成对数据的一个编号列表，从0开始
    int()           将一个字符串或另一个数转换成一个整数，如果可行
    id()            返回一个python数据对象的唯一标识
    next()          返回一个可迭代数据结构（如列表）中的下一项

    toolz:
        模块是一个包含python代码的文本文件
        发布工具允许将模块转换成可共享的包
        setup.py 程序提供了模块的元数据，用来构建、安装、和上传打包的发布
        使用 import 将模块导入到其他程序
        from modle import function
        BIF __builtins__  #built-in function
        print(i;end='') #
        '''注释'''
        #注释
        range（）#返回一个迭代器，根据需要生成一个指定范围的数字
        包含end=‘’作为print() BIF的一个参数会关闭其默认行为（即在输入中自动包含换行）

第三章 文件与异常 #处理错误
    the_file = open('sketch.txt')  #打开
    #do something with the data
    #in "the_file"
    the_file.close()  #关闭

    import os #从标准库导入"os"
    os.getcwd() #获取当前工作目录
    os.chdir('../Mydata/python/chapter3') #切换目录

    data = open('sketch.txt') #打开文件并赋值给data这个对象
    print(data.readline(),end='') #readline获取数据行，print BIF显示它
    data.seek(0) #返回文件起始位置
    data.close() # 打开的文件一定要关闭

    each_line.split(":") #根据 ":" 分解
    (role,line_spoken) = each_line.split(":",1) #分解后多重赋值,查找一次：分为两部分
    each_line.find(":") #在字符串中查找特定子串
    os.path.exists('sketch.txt') #判断文件是否存在

    try/except

        import so
        try:
            data = open('sketch.txt')
            for i in data:
                try:
                    (role,spoken) = i.split(":",1)
                    print(role,end='')
                    print(' said:',end='')
                    print(spoken,end='')
                except ValueError:
                    pass
            data.close()
        except IOError:
            print('the data file is missing')

    toolz：
        open() #BIF打开磁盘文件 #import os
        readline() #从一个打开的文件读取一行
        seek() #可以将文件退回至起始位置
        close() #关闭文件
        ValueError #数据不符合期望的格式时出现
        IOError  #数据无法正常访问时出现
        help()  #BIF 访问帮助文档
        find()  #在字符串中查找特定子串
        not  #关键字 将一个条件取反
        pass #python中的空语句或null语句，它什么也不做
        try/except #提供了一个异常处理机制，从而保护可能运行时错误的某些代码
        tuple #元组 元组是不可变的

第四章 持久存储 #数据保存到文件

    spoken = spoken.strip() #从字符串中去除不想要的空白符
    out = open("data.out","w") #w写 a追加  w+打开文件读写，不清除
    print("py is easy.",file=out)
    out.close()
    locals() BIF #返回当前作用域中定义的所有名字的一个集合
    str(err) #把异常对象’err‘（或强制）转换成字符串

    finally 扩展try 保证文件最终关闭
    with open("man.txt","w") as out_man #with会自动考虑文件状态，最后自动关闭

        try:
            data = open('missing.txt')
            print(data.readline(),end='')
        except IOError as err:
            print('IOError: ' + str(err))
        finally:
            if 'data' in locals():
                data.close()
        ==>

        try:
            with open('sketch.txt') as data:
                print(data.readline(),end='')
        except IOError as err:
            print('IOError: ' + str(err))


    example：
        try:
            out_man = open("man.txt","w")
            out_other = open("other.txt","w")
            print(man,file=out_man)
            print(other,file=out_other)
        except IOError as err:
            print("IOError" + str(err))
        finally:
            if 'out_man' in locals():
                out_man.close()
            if 'out_other' in locals():
                out_other.close()
        ==>
        try:
            with open("man.txt","w") as out_man:
                print(man,file=out_man)
            with open("other.txt","w") as out_other:
                print(other,file=out_other)
        except IOError as err:
            print("IOError" + str(err))
        ==>
        try:
            with open("man.txt","w") as out_man,open("other.txt","w") as out_other:
                print(man,file=out_man)
                print(other,file=out_other)
        except IOError as err:
            print("IOError" + str(err))

    修改printl 保存至文件
        import sys
        def printl(the_list,indent=False,level=0,output=sys.stdout):
            for i in the_list:
                if isinstance(i,list):
                    printl(i,indent,level+1,output)
                else:
                    if indent:
                        for tab_stop in range(level):
                            print("\t",end='',file=output)
                    print(i,file=output)

        import os
        man = []
        other = []
        try:
            with open('sketch.txt') as data:
                for i in data:
                    try:
                        (role,spoken) = i.split(':',1)
                        spoken = spoken.strip()
                        if role == 'Man':
                            man.append(spoken)
                        else:
                            other.append(spoken)
                    except ValueError:
                        pass
        except IOError:
            print('the file do not exists')

        try:
            with open('man.out','w') as outman,open('other.out','w') as outother:
                printl(man,output=outman)
                printl(other,output=outother)
        except IOError as err:
            print('IOError' + str(err))

    pickle #腌制数据

        import pickle

        try:
            with open('man.pickle','wb') as outman,open('other.pinkle','wb') as outother:
                pickle.dump(man,outman)
                pickle.dump(other,outother)
        except IOError as err:
            print('IOError' + str(err))
        except pickle.PickleError as perr:
            print('pickleError' + str(perr))


        newman = []
        try:
            with open('man.pickle','rb') as outnewman:
                newman = pickle.load(outnewman)
        except IOError as err:
            print('IOError' + str(err))
        except pinkle.PickleError as perr:
            print('PickleError' + str(perr))

        printl(newman)

    toolz：
        strip() #方法可以从字符串中去除不想要的空白字符
        print() BIF 中的file控制将数据发送、保存到哪里
        finally 组总会执行 不论 try/except 中出现什么异常
        会向except组传入一个异常对象，并使用 as关键字赋值
        str() BIF 对象转换成字符串
        locals() #BIF 返回当前作用域的变量集合
        in 操作符用于检查成员关系
        '+' 操作符联结两个字符串，数字则相加
        with with语句自动处理打开文件的关闭工作 也使用as关键字
        sys.stdout # import sys
        import pickle #pickle标准库允许容易高效的保存数据 import pickle
        pickle.dump() #将数据保存到磁盘
        pickle.load()　#将数据从磁盘恢复

第五章　推导数据　#处理数据

    #打开选手文件并将其赋值到列表
        try:
            os.chdir('Resources')
            with open('james.txt') as f:
                james = f.readline().strip().split(',')
            with open ('julie.txt') as f:
                julie = f.readline().strip().split(',')
            with open('mikey.txt') as f:
                mikey = f.readline().strip().split(',')
            with open ('sarah.txt') as f:
                sarah = f.readline().strip().split(',')
        except IOError:
            print('the file is missing')


     #定义函数 把列表的时间改成统一格式 .
         def sanitize(time_string):
             if '-' in  time_string:
                 spliter = '-'
             elif '-' in time_string:
                 spliter = ':'
             else:
                 return(time_string)
             (m,s) = time_string.split(spliter)
             return(m + '.' + s)

    upper() #方法转换成大写
    lower() #方法转换成小写
    float() #BIF  转换成浮点数

    print(sorted([sanitize(i) for i in james]))
    #推导列表
        for i the thelist:
            print(i)
        ==>
        [print(i) for i in thelist]

    set() #设置空集合 也可以把列表转换成集合
          #集合是没有重复项的  可以用来去重
    toolz:
        sort() # 列表原地排序 会替换数据
        sort(reverse=True) #复制排序 返回新的列表 加参数是逆序
        new_l = [len(t) for t in old_l] #
        my_list[3:6] #访问列表索引 3-6的数据 不包括 6
        set() #方法创建一个集合

        方法串链 #从左向右读，对数据应用一组方法
        函数串链 #从右往左读，对数据应用一组函数

第六章 定制数据对象  #打包代码与数据
　　
