#!/usr/bin/python
#-*- coding:utf-8 -*-
#cython: language_level=3

import os, sys
import time
import ty_function
import _thread

from tkinter import *
PythonVersion = 3
from tkinter.font import Font
from tkinter.messagebox import *

#所有控件和控件绑定变量引用字典，使用这个字典是为了方便在其他函数中引用所有控件。
gComps = {}
phone_list = ['15081454427', '15081450749', '15127469783', '15081514247', '18831550943', '15246863924', '15127514579', '13458326632', '15127563945', '15033963462','15246865734', '15033311794', '15232529354', '15081522394', '15032421042', '15031444474','15127458615', '15033311449','15081518546', '15127402852', '15081453935', '15892437641', '15127431429', '15373910255', '15128859433','15232427962','15033914298', '15032422551', '15132564225', '15704691184', '15081997514', '15230955024', '15232478504','18832518484', '15132564459', '15232531946', '15103258047', '18784784019', '15127445921','15774699264', '15232453459', '17879349241',  '15127444101', '15246851874',  '15707037834',  '18249408074', '15033326459', '15027549690','18284183858', '15881764072',  '15383215318', '18345854232',  '15027535945',  '15032423427',  '15246857734', '18284166940',  '15734697054','15127445901', '15133969042',  '18345800684', '18304690244',  '15027597340', '15127424225', '15027542656',  '15127460061', '15027575431', '15027468583','15127431355', '15033499047', '15246861864', '15027472994', '18284142553', '15081451053', '15232480247', '15076244737', '15127465743', '15003257264', '15281610994', '15027471529', '15081512604', '18284136469', '15984412272', '15232453637',  '15027468784', '15027472511', '15081526749', '15081535745', '18346930524']

def check(num):
    if int(num) > len(phone_list):
        return -1
    else:
        return 0
'''
def favour():
    count=int(gComps['Text4'].get())

    for i in range(count):
          ty_function.favour_book(phone_list[i],gComps['Text2'].get())
          gComps['Text1'].insert(END,"第"+str(i+1)+"次收藏成功！\n")
          time.sleep(0.5)
'''
def follow():
    count=int(gComps['Text4'].get())

    for i in range(count):
          ty_function.follow(phone_list[i],gComps['Text2'].get())
          gComps['Text1'].insert(END,"第"+str(i+1)+"次关注成功！\n")
          time.sleep(0.5)
'''
def pumpkin():
    count=int(gComps['Text4'].get())

    for i in range(count):
          ty_function.pumpkin(phone_list[i],gComps['Text2'].get())
          gComps['Text1'].insert(END,"第"+str(i+1)+"次南瓜成功！\n")
          time.sleep(0.5)
'''

def Command5_Cmd(event=None):#view
    if check(len(gComps['Text4'].get())) == -1:
        gComps['Text1'].insert(END,"数量太大！请不要超过目前账号数\n")
    pass

def Command3_Cmd(event=None):#评论
    if check(len(gComps['Text4'].get())) == -1:
        gComps['Text1'].insert(END,"数量太大！请不要超过目前账号数\n")
    pass

def Command2_Cmd(event=None):#南瓜
    if check(len(gComps['Text4'].get())) == -1:
        gComps['Text1'].insert(END,"数量太大！请不要超过目前账号数\n")
    else:
        _thread.start_new_thread(pumpkin,())
    pass

def Command1_Cmd(event=None):#收藏
    if check(len(gComps['Text4'].get())) == -1:
        gComps['Text1'].insert(END,"数量太大！请不要超过目前账号数\n")
    else:
        _thread.start_new_thread(favour,())
    pass

def Command4_Cmd(event=None):#关注
    if check(len(gComps['Text4'].get())) == -1:
        gComps['Text1'].insert(END,"数量太大！请不要超过目前账号数\n")
    else:
        _thread.start_new_thread(follow,())
    pass


def main(argv):
    top = Tk()
    top.title('汤圆刷数据')
    top.geometry('496x283')
    gComps['top'] = top

    Command5Font = Font(size=9,weight='bold',slant='roman')
    Command5 = Button(top, text='...', command=Command5_Cmd, font=Command5Font)
    Command5.place(x=352, y=72, width=33, height=25)
    gComps['Command5'] = Command5

    Command3 = Button(top, text='刷评论', command=Command3_Cmd)
    Command3.place(x=400, y=112, width=73, height=33)
    gComps['Command3'] = Command3

    Command2 = Button(top, text='刷南瓜', command=Command2_Cmd)
    Command2.place(x=400, y=16, width=73, height=33)
    gComps['Command2'] = Command2

    Command1 = Button(top, text='刷收藏', command=Command1_Cmd)
    Command1.place(x=400, y=64, width=73, height=33)
    gComps['Command1'] = Command1

    Text2Var = StringVar(value='')
    Text2 = Entry(top, textvariable=Text2Var)
    Text2.place(x=80, y=16, width=305, height=25)
    gComps['Text2'] = Text2
    gComps['Text2Var'] = Text2Var

    Text4Var = StringVar(value='')
    Text4 = Entry(top, textvariable=Text4Var)
    Text4.place(x=80, y=128, width=305, height=25)
    gComps['Text4'] = Text4
    gComps['Text4Var'] = Text4Var

    Text3Var = StringVar(value='')
    Text3 = Entry(top, textvariable=Text3Var)
    Text3.place(x=80, y=72, width=273, height=25)
    gComps['Text3'] = Text3
    gComps['Text3Var'] = Text3Var

    Command4 = Button(top, text='刷关注', command=Command4_Cmd)
    Command4.place(x=400, y=160, width=73, height=33)
    gComps['Command4'] = Command4

    scroll = Scrollbar()
    Text1 = Text(top)
    scroll.pack(side=RIGHT,fill=Y)
    Text1.place(x=8, y=216, width=465, height=57)
    scroll.config(command=Text1.yview)
    Text1.config(yscrollcommand=scroll.set)
    gComps['Text1'] = Text1

    Label4Font = Font(size=15,weight='bold',slant='italic')
    Label4 = Label(top, text='购买账号加QQ：2223513246', fg='#FF0000', anchor='w', font=Label4Font)
    Label4.place(x=88, y=168, width=297, height=33)
    gComps['Label4'] = Label4

    Label3 = Label(top, text='数量：', anchor='w')
    Label3.place(x=32, y=128, width=33, height=17)
    gComps['Label3'] = Label3

    Label2 = Label(top, text='评论词库：', anchor='w')
    Label2.place(x=8, y=80, width=65, height=17)
    gComps['Label2'] = Label2

    Label1 = Label(top, text='书号：', anchor='w')
    Label1.place(x=32, y=24, width=41, height=25)
    gComps['Label1'] = Label1

    top.mainloop()
    try: top.destroy()
    except: pass



if __name__ == "__main__":
    main(sys.argv)
