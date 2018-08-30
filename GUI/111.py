#python3
#tkinter
from tkinter import *

root = Tk()
v = IntVar()
Radiobutton(root,text='One',variable=v,value=1).pack(anchor=W))
Radiobutton(root,text='One',variable=v,value=2).pack(anchor=W))
Radiobutton(root,text='One',variable=v,value=3).pack(anchor=W))
 # value 值不同实现单点
 mainloop(  )


'''
from tkinter import *

root = Tk()
GIRLS = ['Xi','Yang','Wang','Ari']
v = []
for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root,text=girl,variable=v[-1])
    b.pack(anchor=W) #左对齐

root = Tk()
v = IntVar()

c = Checkbutton(root,text='text',variable=v) #选框
c.pack()

l = Label(root,textvariable=v) # 选中后 v 会赋值1
l.pack() #

mainloop()




#------------------
from tkinter import *

def callBack():
    var.set('nothing!')

root = Tk()

frame1 = Frame(root) #框架
frame2 = Frame(root)


var = StringVar()
var.set("FBI warring!") #set 方法设置变量内容
#Label 用来显示文本或图片
textLabel = Label(frame1,
                  textvariable=var, #textvarible 显示字符变量
                  justify=LEFT, #对齐方式
                  padx=10) #边距
textLabel.pack(side=LEFT)

photo = PhotoImage(file='18.gif')
imgLabel = Label(root,image=photo)
imgLabel.pack()

theButton = Button(frame2,text='already 18 years old.',command=callBack)
theButton.pack()
frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()

#----------------
from tkinter import *
root = Tk()

photo = PhotoImage(file='bg.gif')
文字显示在图片上
thelabel = Label(root,
                text="hi there",
                image=photo,
                justify=LEFT,
                compound=CENTER, #
                #font=('微软雅黑',20), #字体字号
                fg="white")
thelabel.pack()
mainloop()

##
from tkinter import *
root = Tk()

#Label 用来显示文本或图片
textLabel = Label(root,text="FBI warring!",
                  justify=LEFT, #对齐方式
                  padx=10) #边距
textLabel.pack(side=LEFT)

photo = PhotoImage(file='18.gif')
imgLabel = Label(root,image=photo)
imgLabel.pack()
mainloop()


##2
import tkinter as tk
class APP():
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT,padx=10,pady=10)

        self.hi_there = tk.Button(frame,text='say hi',bg='black',fg='white',command=self.sayHi)
        self.hi_there.pack()
    def sayHi(self):
        print('hello there!')

root = tk.Tk()
app = APP(root)
root.mainloop()

# 1
import tkinter as tk
app  = tk.Tk()

app.title('Chaogou') #设置标题

thelabel = tk.Label(app,text="窗口") #窗口组件 用来显示文本或图片
thelabel.pack() #自动调节组件自身尺寸

app.mainloop() #主事件循环
'''
