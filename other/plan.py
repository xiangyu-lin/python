#python3
#-*- coding: utf-8 -*-
#

from Toolz import sendEmail
import time

title = 'Todo list'
receivers = ['wevie9@163.com']
data = []
with open('E:\Python\other\plan.txt','r') as f:
    for i in f:
        data.append(i.strip('\n'))

index = data.index(str(time.strftime('%a',time.localtime(time.time()))))
content = data[index + 1] + '\n' + ' \n' + data[index + 2] + '\n' + data[index + 3] + '\n' + data[index + 4]
sendEmail(title,content,receivers)
