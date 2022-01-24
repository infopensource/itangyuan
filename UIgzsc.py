#!/usr/bin/python
#-*- coding:utf-8 -*-
#cython: language_level=3

import os, sys
import time
import ty_function
import _thread
import log_ui

from tkinter import *
PythonVersion = 3
from tkinter.font import Font
from tkinter.messagebox import *

#所有控件和控件绑定变量引用字典，使用这个字典是为了方便在其他函数中引用所有控件。
gComps = {}
phone_list = ['15081454427', '15081450749', '15127469783', '15081514247', '18831550943', '15246863924', '15127514579', '13458326632', '15127563945', '15033963462', '15246865734', '15033311794', '15232529354', '15081522394', '15032421042', '15031444474', '15127458615', '15033311449', '15081518546', '15127402852', '15081453935', '15892437641', '15127431429', '15373910255', '15128859433', '15232427962', '15033914298', '15032422551', '15132564225', '15704691184', '15081997514', '15230955024', '15232478504', '18832518484', '15132564459', '15232531946', '15103258047', '18784784019', '15127445921', '15774699264', '15232453459', '17879349241', '15127444101', '15246851874', '15707037834', '18249408074', '15033326459', '15027549690', '18284183858', '15881764072', '15383215318', '18345854232', '15027535945', '15032423427', '15246857734', '18284166940', '15734697054', '15127445901', '15133969042', '18345800684', '18304690244', '15027597340', '15127424225', '15027542656', '15127460061', '15027575431', '15027468583', '15127431355', '15033499047', '15246861864', '15027472994', '18284142553', '15081451053', '15232480247', '15076244737', '15127465743', '15003257264', '15281610994', '15027471529', '15081512604', '18284136469', '15984412272', '15232453637', '15027468784', '15027472511', '15081526749', '15081535745', '18346930524', '15031440992', '15033397043', '15133984694', '15027583149', '15031444503', '15081505124', '15103154522', '15027472578', '15033997294', '15032433861', '18281714737', '15033964549', '15033314602', '15765169974', '15033914129', '14784691064', '15081452768', '13946692154', '18832505345', '13734506964', '13766687624', '15182357974', '15881797419', '15232489651', '15046917704', '15145917084', '15808171947', '15765150684', '18328339343', '15984656494', '13458321059', '15802646653', '17821011781', '15774697904', '15145906724', '15182409187', '18831556834', '18282019546', '18281785440', '15874808184', '15045733874', '18284191745', '18880405006', '15281733492', '18644044592', '13555102634', '18781703467', '15246875274', '15146992624', '13796904954', '18346919864', '18227350465', '15008174610', '15774692074', '15082194549', '13458446787', '18284127510', '15629561994', '15008184498', '15874997724', '15246860204', '13438402998', '15884639592', '13555171834', '13408109495', '18346930934', '15549520843', '15502726540', '18249439114', '18346912874', '15892491794', '15182930464', '13766672334', '18249432594', '15881734406', '13458024065', '18284159544', '18249422874', '15700234064', '13136229541', '13684693774', '13458300214', '13946688184', '18721430935', '13458013731', '18346902034', '15184670214', '14784692064', '18428002842', '18304694954', '13458064959', '15146991964', '13555108984', '13846900924', '14780459281', '13846990734', '15082191294', '18284174816', '13458074254', '15145915284', '13440007101', '13408166713', '15045716824', '15065419122', '15145914054', '18284198547', '15228726423', '13408115977', '15874892214', '18845306724', '15846780183', '18994959193', '14780499535', '15082768242', '15804534718', '13404009381', '13458322616', '18118096614', '13458326524', '13458065514', '15881730340', '18788951378', '15008176494', '13458325202', '13458087307', '14784699094', '15882897741', '13419126826', '15808411426', '15671123434', '18784743634', '13034274725', '15046906694', '18281976394', '13458305112', '13458061665', '18784278941', '14781657078', '15984600464', '15671123434', '18784743634', '13034274725', '15046906694', '18281976394', '13458305112', '13458061665', '18784278941', '14781657078', '15984600464', '13458003169', '15760581924', '15892751204', '15700224815']

def check(num):
    if int(num) > len(phone_list):
        return -1
    else:
        return 0

def get_comments(path):
    comments=[]
    f= open(path,"r",encoding="utf-8",errors="ignore")
    for each_line in f:
        comments.append(each_line[:-1])
    return comments

def favour():
    count=int(gComps['Text4'].get())

    for i in range(count):
          ty_function.favour_book(phone_list[i],gComps['Text2'].get())
          gComps['Text1'].insert(END,"第"+str(i+1)+"次收藏成功！\n")
          time.sleep(0.5)

def follow():
    count=int(gComps['Text4'].get())

    for i in range(count):
          ty_function.follow(phone_list[i],gComps['Text2'].get())
          gComps['Text1'].insert(END,"第"+str(i+1)+"次关注成功！\n")
          time.sleep(0.5)

def pumpkin():
    count=int(gComps['Text4'].get())

    for i in range(count):
          ty_function.pumpkin(phone_list[i],gComps['Text2'].get())
          gComps['Text1'].insert(END,"第"+str(i+1)+"次南瓜成功！\n")
          time.sleep(0.5)

def comment():
    count=int(gComps['Text4'].get())
    filePath=gComps['Text3'].get()
    comments=get_comments(filePath)

    for i in range(count):
        ty_function.comment(phone_list[i],gComps['Text2'].get(),comments[i])
        gComps['Text1'].insert(END,"第"+str(i+1)+"次评论成功！\n")
        time.sleep(0.5)

def Command5_Cmd(event=None):#view
    if check(len(gComps['Text4'].get())) == -1:
        gComps['Text1'].insert(END,"数量太大！请不要超过目前账号数\n")
    pass

def Command3_Cmd(event=None):#评论
    if check(len(gComps['Text4'].get())) == -1:
        gComps['Text1'].insert(END,"数量太大！请不要超过目前账号数\n")
    else:
        _thread.start_new_thread(comment,())
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
    Label4 = Label(top, text='序列号：2967859260', fg='#FF0000', anchor='w', font=Label4Font)
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
    try:
        top.destroy()
    except: pass



if __name__ == "__main__":
    log_ui.main(sys.argv)
    if log_ui.flag==1:
        main(sys.argv)
