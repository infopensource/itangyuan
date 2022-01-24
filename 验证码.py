from selenium import webdriver     #从selenium库导入webdirver
import phoneNum
import register
import os
import time

#usernames=[]#储存所有注册用的手机号

def register_user():
      browser=webdriver.PhantomJS()    #使用webdirver.PhantomJS()方法新建一个phantomjs的对象，这里会使用到phantomjs.exe，环境变量path中找不到phantomjs.exe，则会报错
     # script = "phantom.setProxy('{ip}', {port})".format(ip='49.79.91.57', port='4256') 
      #browser.execute('EXECUTE_PHANTOM_SCRIPT', {'script': script, 'args': []})

      browser.get("https://www.itangyuan.com/web/register/phone.html")           #使用get()方法，打开指定页面。注意这里是phantomjs是无界面的，所以不会有任何页面显示


      print(browser.get_cookies())
      browser.maximize_window()      #设置phantomjs浏览器全屏显示
      browser.save_screenshot("1.jpg")   #使用save_screenshot将浏览器正文部分截图，即使正文本分无法一页显示完全，save_screenshot也可以完全截图

      register.cut_picture("1.jpg","2.jpg")
      register.grey_picture("2.jpg","grey-2.jpg")
      result=register.baidu_OCR('18450760','6d5C9RntTAE5zVPnDx1CCGZf','TtseDhbyABljTXPwc7EzkoCNQtjaqlea')

      print(result)

      if len(result['words_result'])==0:
            browser.quit()
            return
      if len(result['words_result'][0]['words'].replace(' ',""))!=5:
            browser.quit()
            return
      
      code=result['words_result'][0]['words'].replace(' ',"")
      print(code)

      phone,token=phoneNum.get_phone()

      #usernames.append(phone)#将手机号存入数组

      input_phone = browser.find_element_by_xpath('//*[@id="phone"]')
      input_phone.send_keys(phone[1])

      print(phone)

      input_code = browser.find_element_by_xpath('//*[@id="verification_code"]')
      input_code.send_keys(code)

      Botton_next = browser.find_element_by_xpath('//*[@id="registerForm"]/div[2]/a')
      Botton_next.click()

      vCode=phoneNum.get_phonecode(phone,token)

      print(vCode)

      if vCode == -1:
            a=phoneNum.free_phone(phone,token)
            browser.quit()
            return
      else:
            input_vCode = browser.find_element_by_xpath('//*[@id="vCode"]')
            input_vCode.send_keys(vCode)

            input_sPass = browser.find_element_by_xpath('//*[@id="sPassword"]')
            input_sPass.send_keys('inf123456')

            Botton_ok = browser.find_element_by_xpath('//*[@id="registerForm"]/div[3]/input')
            Botton_ok.click()

            print("success")
            
      #browser.close()
      browser.quit()
      #os.system('killall phantomjs')

      return phone[1]

if __name__=="__main__":
      phonelist=[]
      
      for i in range(40):
            a=register_user()
            if a != None:
                  phonelist.append(a)
            print(a)
      print(phonelist)

'''
'15127431355', '15033499047', '15246861864', '15027472994', '18284142553', '15081451053', '15232480247', '15076244737', '15127465743', '15003257264', '15281610994', '15027471529', '15081512604', '18284136469', '15984412272', '15232453637',  '15027468784', '15027472511', '15081526749', '15081535745', '18346930524']
'''
