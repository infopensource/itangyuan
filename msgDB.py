import sqlite3
import time

#底层通信
def initDB():
      global conn
      conn = sqlite3.connect('exchange.db')
      print ("Opened database successfully")
      
def endDB():
      conn.close()

def sendMsg(token,cmd,id1,id2,id3):
      conn.execute('INSERT INTO WX_COMMAND (TOKEN,CMD_TYPE,ID_1,ID_2,ID_3)\
                   VALUES ("%s", "%s", "%s", "%s","%s")'%(token,cmd,id1,id2,id3))
      conn.commit()
      print ("Records created successfully")

def recMsg():
      result=conn.execute('select * from wx_event limit 0,1')
      return (list(result))

def delMsg():
      conn.execute("delete from wx_event where ID1 in(select ID1 from wx_event limit 1)")
      conn.commit()

def send_wxPicture(wxid,picPath):
      sendMsg('0','wx_picture',wxid,picPath,"null")

#以下函数进行了一次封装
def send_wxMsg(wxid,text):
      sendMsg('0','wx_send',wxid,text,"null")

def listen_wxMsg():
      time.sleep(0.1)
      res=recMsg()
      if len(res)!=0:
            #print(recMsg()[0])
            return recMsg()[0]
      else:
            return False

if __name__=="__main__":
      initDB()
      for i in range(1000):
            delMsg()
      while True:
            res=listen_wxMsg()
            if res==False:
                  continue
            if res[3]=="111":
                  print(res[0])
                  send_wxMsg(res[0],"response")
            if res[3]=="picture":
                  print(res[0])
                  send_wxPicture(res[0],"C:\\1.jpg")
            delMsg()
