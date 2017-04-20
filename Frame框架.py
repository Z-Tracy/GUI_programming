#-*-coding:utf-8-*-
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('350x350+800+400')

tk.Label(master=window,text='on the window').pack()

#定义主框架
frm = tk.Frame(master=window)
frm.pack()
#次框架
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
#side方向基于主frm的
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(master=frm_l,text='on the frm_l1').pack()
tk.Label(master=frm_l,text='on the frm_l2').pack()
tk.Label(master=frm_r,text='on the frm_r1').pack()
window.mainloop()
