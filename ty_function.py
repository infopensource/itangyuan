import requests
import time
#cython: language_level=3

def favour_book(phone,booknum):
      requests.packages.urllib3.disable_warnings()#remove warning

      password='inf123456'

      post={'password':password,
            'unique_id':"dW5pcXVlX2lkOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLUg1SU5JVERFVklDRQ==",
            'app_version':"YXBwX3ZlcnNpb246YW5kcm9pZC01MDUyMA==",
            'phone':phone}

      session = requests.Session()
      response=session.post("https://i.itangyuan.com/login/phone.json",data=post,verify=False)


      favour=session.get('http://m.itangyuan.com/user/favor/'+booknum+'.json')
      #unfavour=session.get('http://m.itangyuan.com/user/unfavor/5948396.json')


def follow(phone,usernum):
      requests.packages.urllib3.disable_warnings()#remove warning

      password='inf123456'

      post={'password':password,
            'unique_id':"dW5pcXVlX2lkOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLUg1SU5JVERFVklDRQ==",
            'app_version':"YXBwX3ZlcnNpb246YW5kcm9pZC01MDUyMA==",
            'phone':phone}

      session = requests.Session()
      response=session.post("https://i.itangyuan.com/login/phone.json",data=post,verify=False)


      favour=session.get('http://i.itangyuan.com/friend/follow/'+usernum+'.json')
      #print(favour.text)


def pumpkin(phone,booknum):
      requests.packages.urllib3.disable_warnings()#remove warning

      password='inf123456'

      post={'password':password,
            'unique_id':"dW5pcXVlX2lkOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLUg1SU5JVERFVklDRQ==",
            'app_version':"YXBwX3ZlcnNpb246YW5kcm9pZC01MDUyMA==",
            'phone':phone}

      session = requests.Session()
      response=session.post("https://i.itangyuan.com/login/phone.json",data=post,verify=False)


      favour=session.get('http://m.itangyuan.com/book/send/pumpkin/'+booknum+'/1.json')


def comment(phone,booknum,comments):
      #print(comments)
      requests.packages.urllib3.disable_warnings()#remove warning

      password='inf123456'

      post={'password':password,
            'unique_id':"dW5pcXVlX2lkOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLUg1SU5JVERFVklDRQ==",
            'app_version':"YXBwX3ZlcnNpb246YW5kcm9pZC01MDUyMA==",
            'phone':phone}

      comment_post={'title':'发表新评论',
            'content':comments}

      session = requests.Session()
      response=session.post("https://i.itangyuan.com/login/phone.json",data=post,verify=False)

      favour=session.post('http://i.itangyuan.com/comment/release/'+booknum+'.json',data=comment_post)
      #print(favour.text)

'''
phone_list=['15127458615', '15081518546', '15127402852', '15081453935', '15892437641', '15127431429', '15373910255', '15128859433','15232427962',  '15033914298', '15032422551', '15132564225',  '15704691184']

for i in phone_list:
      follow(i,'6000899')
      print('success')
      time.sleep(1)
'''

