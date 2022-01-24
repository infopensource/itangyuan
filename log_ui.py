#!/usr/bin/python
#-*- coding:utf-8 -*-

import os, sys
import login
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()


#所有控件和控件绑定变量引用字典，使用这个字典是为了方便在其他函数中引用所有控件。
gComps = {}
top = Tk()
flag=0


def Command1_Cmd(event=None):
    a=gComps['Text2'].get()
    b=login.regNum(login.computerNum())
    if b==a:
        global flag
        flag=1
    top.destroy()


def main(argv):
    top.title('登录')
    top.geometry('303x124')
    top.resizable(0,0)
    gComps['top'] = top

    Command1 = Button(top, text='登录', bg='#00FF00', command=Command1_Cmd)
    Command1.place(x=248, y=16, width=41, height=65)
    gComps['Command1'] = Command1

    Text2Var = StringVar(value='')
    Text2 = Entry(top, textvariable=Text2Var)
    Text2.place(x=56, y=56, width=177, height=25)
    gComps['Text2'] = Text2
    gComps['Text2Var'] = Text2Var

    Text1Var = StringVar(value=login.computerNum())
    Text1 = Entry(top, textvariable=Text1Var)
    Text1.place(x=56, y=16, width=177, height=25)
    gComps['Text1'] = Text1
    gComps['Text1Var'] = Text1Var

    Label2 = Label(top, text='注册码', anchor='w')
    Label2.place(x=8, y=56, width=41, height=17)
    gComps['Label2'] = Label2

    Label1 = Label(top, text='随机码', anchor='w')
    Label1.place(x=8, y=16, width=41, height=17)
    gComps['Label1'] = Label1

    Label3Font = Font(size=12,weight='bold',slant='italic')
    Label3 = Label(top, text='联系qq:2223513246获取注册码', fg='#FF0000', anchor='w', font=Label3Font)
    Label3.place(x=32, y=96, width=241, height=25)
    gComps['Label3'] = Label3

    top.mainloop()
    try: top.destroy()
    except: pass


if __name__ == "__main__":
    main(sys.argv)
