#-*-coding:utf-8-*-
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

var= tk.StringVar()

l = tk.Label(master=window,bg='yellow',width=25,text='empty')

l.pack()

def print_selection():
    #所以的参数都是可以改变的
    l.config(text='you have selected' + var.get())
r1 = tk.Radiobutton(master=window,text='Option A',variable=var,value='A',command=print_selection)#vard的值存放在value
r1.pack()

r2 = tk.Radiobutton(master=window,text='Option B',variable=var,value='B',command=print_selection)#vard的值存放在value
r2.pack()

r3 = tk.Radiobutton(master=window,text='Option C',variable=var,value='C',command=print_selection)#vard的值存放在value
r3.pack()

window.mainloop()