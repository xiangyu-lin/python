# 廖雪峰 Python3教程笔记
#
基础
    数据类型和变量
        '\ ' #  转义
        print(r'a\b') #r'' 不转义
        None #空值 不是0
        True False and or not #布尔值可以用与或非运算
        >>> 23%4   3 #求余
        >>> 10//3  3 #地板除 只取整
    字符串和编码
        ord() #函数获取字符的整数表示
        chr() #函数把编码转换为对应的字符
        len() #函数要计算str包含多少个字符
        # -*- coding: utf-8 -*- #程序中包含中文字符 指定utf-8编码
        格式化
            占位符
            'Hi, %s, you have $%d.' % ('Michael', 1000000) #格式化输出
                    #%d	整数      #%s	字符串
                    #%f	浮点数    #%x	十六进制整数
            print('%2d-%02d' % (3, 1)) #空两格-补一个0
             3-01
            >>> print('%.2f' % 3.1415926) #显示小数点两位
            3.14

            format()
            >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
    使用list和tuple #列表和元组
        #Python 从0 开始记数
        #list 列表
        list1 = ['1','2','3',['4.1','4.2','4.3']] #列表赋值
        list1[0] #列表第一个元素
        list1[-1] #倒数第一
        list1[3][2] '4.3'
        list1.append('4') #追加元素到列表末尾
        list1.insert(0,'0') #在某位置插入
        list1.pop() #末尾删除一个元素
        list1[1] = '9' #替换该位置元素
        list1.extend('3','4') #末尾插入列表
        #tuple 元组
        tuple1 = ('1','2','3')
        tuple1[0] # '1'
        tuple1[-1] # '3'
        tuple1 = ('1',) #tuple 只定义一个元素时要用逗号','
        tuple #元组是不可变的但是元组包含list 其中list可变 但list还是那个list
    条件判断
        if x:
            print('True')
        #只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
        age = int(input('Enter age:'))
        if age < 18:
            print('kid')
        elif age >= 18 and age <= 60:
            print('adult')
        else:
            print('old')
    循环
        for i in range(101): #range() 生成 0-100
            if int(i) <= 97:
                print(i)
            elif i == 98:
                continue #跳过当前的这次循环，直接开始下一次循环
            elif i == 99:
                print(i)
            else:
                break   #循环过程中直接退出循环

        a = 0
        while True:
            if a == 20:
                print(a)
                break
            a += 1
    dict和set
        dict #字典
        d = {'Michael': 95, 'Bob': 75, 'Tracy': 85} #创建
        d.get('Thomas') # 判断key是否存在
        d.get('Thomas', -1) #-1为不存在的自定义返回值
        d.pop('Bob')   #删除 Bob 的键值
        set #集合
        set 自动过滤重复项
        s = set([1, 2, 3])
        s.add(4) #增加
        s.remove(4) #删除
函数
    调用函数
        abs(-12) #调用abs函数求绝对值
        max() #max() 函数接受多个数值 返回最大的
        int('12.3') # 转换成整数
        float(12) #浮点数
        str(123) #字符串
        bool(1) #布尔型
        hex() #转换成16进制
    定义函数
        def nop(): #定义空函数
            pass #pass 语句什么都不做 也可以用在其他语句里
        def enroll(name,age=6,birth=True,hobby=['1','2','3']):
            '''name必须给定 age,birth,hobby 定义的默认参数.

            可以是列表或者其他类型,默认参数必须指向不可变对象'''
            print(name,age,birth,hobby)
    函数参数
        def funC(x,n): #x,n 为位置参数
            print(x*n)
        def funC(x,n=2): #n 为默认参数
            return x*n #函数的返回值用return

    递归函数 #内部调用本身
        def fact(n):
            if n==1:
                return
            return n * fact(n-1)
高级特性
    切片 #字符串也可以切片
        L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
        L[-1]  #倒一    #-2倒2
        L[0:3] #从索引0取到3 但不包括3
        L[:10] #取前10
        L[-10:] #后10个数
        L[10:20] #11-20
        L[:10:2] #前10 每两个取一个 02468
        L[::2] #所有数 每2个取一个
    迭代
        L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
        from collections import Iterable
        isinstance(L,Iterable)

        enumerate() #函数可以把一个list变成索引-元素对
            >>> for i,value in enumerate(L):
            ...     print(i,value)
            ...
            0 Michael
            1 Sarah
            2 Tracy
            3 Bob
            4 Jack
    列表生成式[推导列表]
        list(range(1, 11)) #生成1-10
        [x * x for x in range(1, 11)] #推导列表
        [x * x for x in range(1, 11) if x % 2 == 0] #循环

    生成器
        next()
    迭代器
        from collections import Iterator
        isinstance((x for x in range(10)), Iterator)
函数式编程
    高阶函数 #Higher-order function
        变量可以指向函数本身
            f = abs
            f(-10)
            10
            def add(x, y, f):
                return f(x) + f(y) #abs(x) + abs(y)
        map() 和 reduce()
            map() #函数接收两个参数，一个是函数，一个是Iterable 将传入的函数依次
                  #作用到序列的每个元素，并把结果作为新的Iterator返回。
                list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
            reduce() #educe把一个函数作用在一个序列[x1, x2, x3, ...]上，
                     #这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
                >>> from functools import reduce
                >>> def fn(x, y):
                ...     return x * 10 + y
                ...
                >>> reduce(fn, [1, 3, 5, 7, 9])
                13579
        filter() #函数用于过滤序列。
            #filter()也接收一个函数和一个序列。和map()不同的是，
            #filter()把传入的函数依次作用于每个元素，
            #然后根据返回值是True还是False决定保留还是丢弃该元素。
            def isOdd(n):
                return n%2==1
            l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            list(filter(isOdd,l2)) #过滤出奇数
        sorted() #它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
            sorted([36, 5, -12, 9, -21], key=abs)
            sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) #忽略大小写排序
            sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True) #反向
    返回函数
        函数作为返回值
            def lazy_sum(*args):
                def sum():
                    ax = 0
                    for n in args:
                        ax = ax + n
                    return ax
                return sum

基础
数据类型
组合数据类型
控制结构与函数
    控制结构
    异常处理
    自定义函数
模块
面向对象
文件处理
    pickle
    写入与分析
    xml文件
高级
调试
进程与线程
网络
数据库
正则
GUI
