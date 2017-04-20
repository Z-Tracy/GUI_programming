#-*-coding:utf-8-*-
import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('300x300')

l =tk.Label(master=window,width=25,bg='yellow',text='empty')
l.pack()

def print_selection():
    if(var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif(var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif(var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

var1 =tk.IntVar()
var2 =tk.IntVar()
#选定Pythonvariable将绑定，onvalue=1,offvalue=0,此时=1会赋值给var1
c1 = tk.Checkbutton(master=window,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c2 = tk.Checkbutton(master=window,text='C++',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2.pack()

window.mainloop()