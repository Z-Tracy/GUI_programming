#-*-coding:utf-8-*-
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('350x350+800+400')

l = tk.Label(master=window,text='',bg='yellow')
l.pack()

count=0
def do_job():
    global count
    #config改变Label的参数
    l.config(text='do'+str(count))
    count+=1
#定义Mwnu顶级菜单
menubar = tk.Menu(master=window)
#tearoff设置为1时表示菜单可独立出来，或者False
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
#表示加条分割线
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=filemenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

#在filemenu中创建多级菜单
submenu = tk.Menu(filemenu,tearoff=False)
#underline,指字体下划线，如果1（True)则加下划线默认为0（Fasle）
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu1',command=do_job)


#显示菜单
window.config(menu=menubar)
window.mainloop()