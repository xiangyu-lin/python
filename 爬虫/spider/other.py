#  -*- coding: utf-8 -*- #程序中包含中文字符 指定utf-8编码

print(data.readline(),end='') #readline获取数据行，输入中自动换行
in 操作符用于检查成员关系
pickle.dump
pickle.load
pickle 的默认格式是二进制格式
可以使用 pickle 模块把 Python 对象直接保存到文件里，而不需要先把它们转化为字符串再保存，也不需要用底层的文件访问操作把它们写入到一个二进制文件里。
pickle 模块会创建一个 Python 语言专用的二进制格式，不需要使用者考虑任何文件细节，它会帮你干净利索地完成读写对象操作，唯一需要的只是一个合法的文件句柄。
用pickle比你打开文件、转换数据格式并写入这样的操作要节省不少代码行。

eval(node_post) #转换字典列表
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
