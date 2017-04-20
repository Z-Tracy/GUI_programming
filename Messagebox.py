#-*-coding:utf-8-*-
import tkinter as tk
import tkinter.messagebox as msgbox
window = tk.Tk()
window.title('my window')
window.geometry('350x350+800+400')


def hit_me():
    #tk.messagebox.showinfo(title='Hi',message='hahaha')这样表示会报错，我也不理解
    #弹出消息对话框提示
    # msgbox.showinfo(title='Hi',message='hahaha')
    #弹出消息对话框警告
    msgbox.showwarning(title='Hi',message='Fuck!')
    #弹出消息对话框报错
    msgbox.showerror(title='Hi',message='ERROR!!')
    #弹出消息对话框,返回值为YES或NO
    msgbox.askquestion(title='Hi',message='ERROR!!')

tk.Button(master=window,text='hit me',command=hit_me).pack()

window.mainloop()