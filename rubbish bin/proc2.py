import numpy as np
import cv2
import matplotlib.pyplot as plt
import register
 
img = cv2.imread('c2.jpg',1)#cv2中imread将彩色图像rgb格式读取成bgr格式
b,g,r=cv2.split(img)#先将bgr格式拆分
img=cv2.merge([r,g,b]);#再将通道按rgb方式组合，这样在matplotlib中默认按rgb格式读取图像即可显示出彩色图像
 
# 中值滤波
img_median = cv2.medianBlur(img,13)


cv2.imwrite("d2.jpg",img_median)

