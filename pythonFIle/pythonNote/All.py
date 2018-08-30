#
数据类型和变量


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
