#-*-coding:utf-8-*-
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

var1 =tk.StringVar()
label = tk.Label(master=window,bg='yellow',width=5,textvariable=var1)
label.pack()

#insert可以指定插入到你所指定的位置，在文本框中鼠标所指位置将会作为插入地址
def print_selection():
    #表示光标所选定的东西
    value = lb.get(lb.curselection())
    var1.set(value)


button1 = tk.Button(master=window,text='print selection',width= 15,height=2,command=print_selection)
button1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(master=window,listvariable=var2)

list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()


t= tk.Text(master=window,height=2)
t.pack()
window.mainloop()