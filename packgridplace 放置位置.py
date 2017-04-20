#-*-coding:utf-8-*-
#注意：不要试图在一个主窗口中混合使用pack和grid
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200+450+350')

# for i in range(4):
#     for j in range(3):
#         #pady表示y轴间距为10
#         tk.Label(master=window,text=1).grid(row=i,column=j,pady=10,padx=10)

#place表示放在单独的坐标,较为精准
# tk.Label(master=window,text=1).place(x=10,y=100,anchor='nw')
tk.Label(master=window,text=1).pack(side='top')
tk.Label(master=window,text=2).pack(side='bottom')
tk.Label(master=window,text=3).pack(side='left')
tk.Label(master=window,text=4).pack(side='right')

window.mainloop()