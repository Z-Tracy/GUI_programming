#-*-coding:utf-8-*-
'''
你同样可以指定控件跨越一个或者多个网格。columnspan选项可以指定控件跨越多列显示，
而rowspan选项同样可以指定控件跨越多行显示。
下面的代码创建了我们最初演示的示意图：
'''
from tkinter import *

master = Tk()
var = IntVar()

Label(master, text="First").grid(sticky=E)
Label(master, text="Second").grid(sticky=E)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

checkbutton = Checkbutton(master, text='Preserve aspect', variable=var)
checkbutton.grid(columnspan=2, sticky=W)

photo = PhotoImage(file='2qq.gif')
label = Label(image=photo)
label.image = photo
label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

button1 = Button(master, text='Zoom in')
button1.grid(row=2, column=2)

button2 = Button(master, text='Zoom out')
button2.grid(row=2, column=3)

mainloop()

'''
在这段代码中，有一些细节需要注意：
1. 我们没有为左边的两个label控件指定具体的位置，在这种情况下，column将会从0开始，而row将会从第一个没有使用的值开始。
2. 我们队checkbutton设置了columnspan参数，所以它会显示在第二行，并占据第0和1列。
3. 图像label占用了2行2列，而最后的两个button都只占用了1列。
'''