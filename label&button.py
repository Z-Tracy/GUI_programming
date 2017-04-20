#-*-coding:utf-8-*-
import tkinter as tk
window = tk.Tk()
#窗口名字
window.title("my window")
#窗口大小
window.geometry('300x100')

#将字符串的变量表示tk中特定的形式
var = tk.StringVar()
#传入窗体对象，显示文本，背景颜色，字体,label长高
label =tk.Label(master=window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)

label.pack()

on_hit = False

def hit_me():
    global on_hit
    #以下条件判断点击一次显示var.set 第二次不显示
    if on_hit == False:
        on_hit = True
        #将字符串设置为
        var.set('you hit me')
    else:
        on_hit =False
        var.set('')
    #点击将会执行command所传的函数
button = tk.Button(master=window,text="hit me",width=15,height=2,command=hit_me)
button.pack()
window.mainloop()