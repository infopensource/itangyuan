#!/usr/bin/python
#-*- coding:utf-8 -*-
import time
import os, sys
import ty_function
import _thread

from tkinter import *
PythonVersion = 3
from tkinter.font import Font
from tkinter.messagebox import *
#import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog    #askstring()


#所有控件和控件绑定变量引用字典，使用这个字典是为了方便在其他函数中引用所有控件。
gComps = {}


def thread_it(func, *args):
  '''将函数打包进线程'''
  # 创建
  t = threading.Thread(target=func, args=args) 
  # 守护 !!!
  t.setDaemon(True) 
  # 启动
  t.start()

def Command1_Cmd(event=None):
    _thread.start_new_thread(favour,())

def favour():
    phone_list=['15127458615', '15081518546', '15127402852', '15081453935', '15892437641', '15127431429', '15373910255', '15128859433','15232427962',  '15033914298', '15032422551', '15132564225',  '15704691184']

    for i in phone_list:
          ty_function.favour_book(i,gComps['Text1'].get())
          time.sleep(0.5)


def main(argv):
    top = Tk()
    top.title('刷收藏（试用版）')
    top.geometry('306x84')
    gComps['top'] = top

    Label1Font = Font(size=16,weight='bold',slant='roman')
    Label1 = Label(top, text='作者QQ：2223513246', fg='#FF0000', anchor='w', font=Label1Font)
    Label1.place(x=48, y=48, width=273, height=33)
    gComps['Label1'] = Label1

    Label2 = Label(top, text='书号：', anchor='w')
    Label2.place(x=16, y=16, width=41, height=25)
    gComps['Label2'] = Label2

    Text1Var = StringVar(value='')
    Text1 = Entry(top, textvariable=Text1Var)
    Text1.place(x=64, y=16, width=153, height=18)
    gComps['Text1'] = Text1
    gComps['Text1Var'] = Text1Var

    Command1 = Button(top, text='刷', command=Command1_Cmd)
    Command1.place(x=232, y=16, width=41, height=17)
    gComps['Command1'] = Command1

    top.mainloop()
    try: top.destroy()
    except: pass



if __name__ == "__main__":
    main(sys.argv)
