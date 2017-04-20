#-*-coding:utf-8-*-
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(master=window,bg='blue',height=100,width=200)
#打开存放的图片
image_file = tk.PhotoImage(master=window,file='2qq.gif')

#定义所放画布的点
image = canvas.create_image(10,10,anchor='nw',image=image_file)
x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
canvas.pack()

b = tk.Button(master=window,text='move').pack()
window.mainloop()