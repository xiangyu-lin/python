#Windows python3
# -*- coding: utf-8 -*-
import sys
import os
import time

def printl(the_list,output=sys.stdout):
    for i in the_list:
        if isinstance(i,list):
            printl(i,output)
        else:
            if str(i) == 'EOF\n':  #只保留 EOF以上的内容
                break
            print(i.strip('\n'),file=output)

month =  time.strftime("%Y-%m", time.localtime()) #获取当前月份 2018-02
today =  time.strftime("%Y-%m-%d", time.localtime()) #获取年月日 2018-02-02

os.chdir('E:\working directory\文件\工作记录')
if os.path.exists(month):
    os.chdir(month)
else:
    os.mkdir(month)
    os.chdir(month)

with open('E:\working directory\待办.md','r',encoding='UTF-8') as f_note:  #unicodedecodeerror: 'gbk'
    note = list(f_note)
    with open(today + '.md','w',encoding='UTF-8') as f:
        printl(note,output=f)

print('Work Note Save Success!')

with open(today + '.md','r',encoding='UTF-8') as f:
    p = list(f)
    printl(p)
