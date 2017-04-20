#-*-coding:utf-8-*-
@Time : 2017.4.12
@Author : 哆啦AOA
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import webbrowser
import re

class Window:
    def __init__(self, title='VIP视频破解测试版', width=420, height=250):
        self.w = width
        self.h = height
        self.root = tk.Tk(className=title)

        frame_1 = Frame(self.root)
        frame_1.pack()

        self.b1 = IntVar()

        bt1 = tk.Checkbutton(frame_1,text='通道一',variable =self.b1,width=12, height=3)
        bt1.grid(row = 1, column = 1)
        self.b2 = IntVar()
        bt2 = tk.Checkbutton(frame_1,text='通道二', variable =self.b2, width=12, height=3)
        bt2.grid(row = 1, column = 2)


        self.b3 = IntVar()
        bt3 = tk.Checkbutton(frame_1,text='通道三',variable =self.b3,width=12, height=3)
        bt3.grid(row = 1, column = 3)

        frame2 = Frame(self.root)
        frame2.pack()
        label = Label(frame2, text = "请输入播放链接")
        self.url = StringVar()
        entry = Entry(frame2, textvariable = self.url,highlightcolor = 'red', highlightthickness = 1)
        play = Button(frame2, text = "播放",width=5, height=2 ,command = self.confirm)

        label.grid(row = 5,column=1)
        entry.grid(row = 5, column = 2)
        play.grid(row = 5, column = 3,ipadx=5, ipady=5)


        menu = Menu(master=self.root)

        filemenu = Menu(menu,tearoff=0)
        menu.add_cascade(label='关于',menu=filemenu)
        filemenu.add_command(label='留言反馈',command=lambda :webbrowser.open('http://blog.csdn.net/qq_35755357'))

        filemenu.add_command(label='Exit',command=self.root.quit)
        self.root.config(menu=menu)


        frame3 = Frame(self.root)
        frame3.pack()
        label_explain = Label(master=frame3,bg='HotPink',text='通道支持:爱奇艺,搜狐,优酷,腾讯,乐视,芒果,bilibili,PPTV,土豆\n若播放失败请选择刷新或其他通道观看')
        label_explain.grid(row = 5, column = 0)


        frame4 = Frame(self.root)
        frame4.pack()
        label_warning = Label(master=frame4,font=('Arial',11),bg='Yellow',text='警告：本软件仅供学习交流，严禁用作商业用途')
        label_warning.grid(row = 6, column = 0)

        frame5 = Frame(self.root)
        frame5.pack()
        label_warning = Label(master=frame5,font=('Arial',11),text='作者:哆啦AOA')
        label_warning.grid(row = 6, column = 0)

        frame6 = Frame(self.root)
        frame6.pack()
        label_QQ = Label(master=frame6,font=('Arial',11),text='QQ一群582318817\nQQ二群343245856')
        label_QQ.grid(row = 7, column = 0)





    def center(self):

        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int( (ws/2) - (self.w/2) )
        y = int( (hs/2) - (self.h/2) )

        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))



    def confirm(self):

        port_1 = 'https://api.47ks.com/webcloud/?v='
        port_2 = 'http://www.wmxz.wang/video.php?url='
        port_3 = 'http://www.vipjiexi.com/yun.php?url='
        #正则表达是判定是否为合法链接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):==

            #限定每次仅可以选择一个通道
            if (self.b1.get() + self.b2.get() + self.b3.get()) !=1:

                msgbox.showwarning(title='警告',message='请选择一个通道！')


            elif self.b1.get() == True:

                webbrowser.open(port_1 + self.url.get())



            elif self.b2.get() == True:
                webbrowser.open(port_2 + self.url.get())


            else:
                self.b3.get() == True

                webbrowser.open(port_2 + self.url.get())

        else:
            msgbox.showerror(title='错误',message='这不是一个有效链接!')


    def loop(self):
        self.root.resizable(False, False)   #禁止修改窗口大小
        self.center()                       #窗口居中
        self.root.mainloop()

if __name__ == '__main__':
    w = Window()
    w.loop()
