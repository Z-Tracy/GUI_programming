#-*-coding:utf-8-*-
import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

#show表示输入的字符显示为你所指定的，隐藏功能
entry = tk.Entry(master=window,show='*')
entry.pack()
#insert可以指定插入到你所指定的位置，在文本框中鼠标所指位置将会作为插入地址
def insert_point():
    var = entry.get()
    t.insert('insert',var)

def insert_end():
    var = entry.get()
    t.insert('end',var)
   # t.insert(1.1,var)#表示在第一行第一列插入
button1 = tk.Button(master=window,text='insert point',width= 15,height=2,command=insert_point)
button1.pack()
button2 = tk.Button(master=window,text='insert end',command=insert_end)
button2.pack(padx=20, side='left')
t= tk.Text(master=window,height=2)
t.pack()
window.mainloop()