#!/usr/bin/python
#-*- coding:utf-8 -*-
#cython: language_level=3

'''
接口说明：
1.收藏    python main_func.py favour 书号 数量
2.关注    python main_func.py follow 用户号 数量
3.南瓜    python main_func.py pumpkin 书号 数量
4.评论    python main_func.py comment 书号 数量 评论内容
'''

import base64
import os, sys
import time
import ty_function

#所有控件和控件绑定变量引用字典，使用这个字典是为了方便在其他函数中引用所有控件。
phone_list = []
argv=sys.argv
print(argv)

def from_base64(string):#不用管，依赖函数
      return str(base64.b64decode(string))[2:-1]

def get_phone(path):#初始化,返回账号列表
    f= open(path,"r",encoding="utf-8",errors="ignore")
    phone=[]
    
    for each_line in f:
          phone.append(from_base64(str(each_line[:-1]+"=").replace(' ','')))
    f.close()
    return phone

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

def favour(count,phone_list,booknum):
    for i in range(count):
          ty_function.favour_book(phone_list[i],booknum)
          #gComps['Text1'].insert(END,"第"+str(i+1)+"次收藏成功！\n")
          time.sleep(0.5)
    return 0

def follow(count,phone_list,usernum):
    for i in range(count):
          ty_function.follow(phone_list[i],usernum)
          #gComps['Text1'].insert(END,"第"+str(i+1)+"次关注成功！\n")
          time.sleep(0.5)
    return 0

def pumpkin(count,phone_list,booknum):
    for i in range(count):
          ty_function.pumpkin(phone_list[i],booknum)
          #gComps['Text1'].insert(END,"第"+str(i+1)+"次南瓜成功！\n")
          time.sleep(0.5)
    return 0

def comment(count,filePath,booknum):#参数 ：数量，词库名
    comments=get_comments(filePath)

    for i in range(count):
        ty_function.comment(phone_list[i],booknum,comments[i])
        gComps['Text1'].insert(END,"第"+str(i+1)+"次评论成功！\n")
        time.sleep(0.5)
    return 0

def exchange():#接口
      if argv[1]=="favour":
            favour(int(argv[3]),phone_list,argv[2])
      if argv[1]=="follow":
            follow(int(argv[3]),phone_list,argv[2])
      if argv[1]=="pumpkin":
            pumpkin(int(argv[3]),phone_list,argv[2])
      if argv[1]=="comment":
            comment(int(argv[3]),phone_list,argv[2])

if __name__=="__main__":
      phone_list=get_phone('1.txt')
      exchange()

