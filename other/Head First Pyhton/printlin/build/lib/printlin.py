#Windows python3
#nester

#迭代打印列表函数
def printl(the_list):
    ''' 使用for循环打印列表内容.

    i in list 如果 i 也是列表，再调用自身循环输出i'''
    for i in the_list:
        if isinstance(i,list):
            printl(i)
        else:
            print(i)
