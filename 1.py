from selenium import webdriver
 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 

proxy = [
 
'--proxy=%s' % "180.122.38.249:4253", # 设置的代理ip
 
'--proxy-type=http', # 代理类型
 
'--ignore-ssl-errors=true', # 忽略https错误
 
]
 
 
 
# 在初始化浏览器对象的时候可以接收一个service_args的参数，使用这个参数设置代理
 
drive = webdriver.PhantomJS(service_args=proxy)
 
 
 
# 设置页面加载和js加载超时时间，超时立即报错，如下设置超时时间为10秒
 
drive.set_page_load_timeout(10)
 
drive.set_script_timeout(10)
 
 
 
# 这样代理就设置成功了，可以向百度发送请求验证ip是否可用
 
drive.get('http://www.baidu.com')
