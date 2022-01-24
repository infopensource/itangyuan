import cv2 as cv
import numpy as np

src=cv.imread(r'2.jpg')
cv.namedWindow('input',cv.WINDOW_AUTOSIZE)
cv.imshow('input',src)

h,w=src.shape[:2]
print(h,w)
'''
dst=cv.resize(src,(186,69),fx=0.75,fy=0.75,interpolation=cv.INTER_NEAREST) #最近邻插值法 cv.INTER_NEAREST
cv.imshow(‘INTER_LINEAR’,dst)
#图像尺寸变换cv2.resize()
#使用cv2.resize时，参数输入是宽×高×通道
#例如：new_img = cv2.resize(img, (800, 500), interpolation=cv2.INTER_CUBIC)

dst=cv.resize(src,(186,69,interpolation=cv.INTER_LINEAR) #双线性插值法 cv.INTER_LINEAR
cv.imshow(‘INTER_LINEAR’,dst)
'''
interpolation=cv.INTER_CUBIC


dst=cv.resize(src,(372,138),interpolation=cv.INTER_CUBIC) #双三次插值法 cv.INTER_CUBIC
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #定义一个核
dst = cv.filter2D(dst, -1, kernel=kernel)
cv.imshow('INTER_LANCZOS4',dst)

cv.imwrite("c2.jpg",dst)

cv.waitKey(0)
cv.destroyAllWindows()
