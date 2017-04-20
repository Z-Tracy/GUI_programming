#-*-coding:utf-8-*-
'''
使用sticky参数
默认的空间会在网格中居中显示。你可以使用sticky选项去指定对齐方式，可以选择的值有：
N/S/E/W，分别代表上/下/左/右。
如果你想让label靠左显示，你可以设置stricky的值为W。
'''
from tkinter import *

master = Tk()
Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)


e1 = Entry(master)
e2 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()