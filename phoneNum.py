import requests
import time
import re

def get_phone():
      #获取token
      token=requests.get("http://api.myzjxl.com:8080/Login/?username=hacktor&password=li17721387472").text
      token=token.split("|")[1]

      gdata={'id':"13083",
             'token':token,
             'card':2
            }

      phone=requests.post("http://api.myzjxl.com:8080/GetPhone/?id=13083&token="+token,data=gdata).text.split('|')
      #http://api.myzjxl.com:8080/Cancel/?id=项目ID&phone=手机号码&token=登录返回token
      #print(phone[1])
      return phone,token

def get_phonecode(phone,token):
      code=['0']
      count=0

      time.sleep(10)

      while (code[0]=='0'):
            count+=1
            code=requests.get("http://api.myzjxl.com:8080/GetMsg/?id=13083&phone="+phone[1]+"&token="+token).text.split('|')
            print(code)
            time.sleep(6)
            if count>5:
                  return -1
                  break

      num = re.findall('\d+',code[1])

      return num[0]

def black_phone(phone,token):
      result=requests.get("http://api.myzjxl.com:8080/Addblack/?id=13083&phone="+phone[1]+"&token="+token).text.split('|')
      if result[0]==1:
            return 1
      else:
            return result

def free_phone(phone,token):
      result=requests.get("http://api.myzjxl.com:8080/Cancel/?id=13083&phone="+phone[1]+"&token="+token).text.split('|')
      if result[0]==1:
            return 1
      else:
            return result
