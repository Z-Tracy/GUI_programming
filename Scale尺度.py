#-*-coding:utf-8-*-
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

l = tk.Label(master=window,bg='yellow',width=25,text='empty')

l.pack()

def print_selection(v):
    l.config(text='you have selected'+ v)

#进度条的名字和取值范围,orient=tk.HORIZONTAL表示方向为横向,像素宽度200,showvalue表示每次拖动显示数值,tickinterval标签间隔长度,resolution表示保留两位小数
s = tk.Scale(master=window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=3,resolution=0.01,command=print_selection)
s.pack()
window.mainloop()