from PIL import Image
from aip import AipOcr
import cv2

#截取验证码部分
def cut_picture(openPicturePath,savePicturePath):
      img = Image.open(openPicturePath)
      cropped = img.crop((550, 281, 612, 304))  # (left, upper, right, lower) 左上，右下
      #Image._show(cropped)
      cropped=cropped.convert('RGB')
      cropped.save(savePicturePath)

def grey_picture(openPicturePath,savePicturePath):
      #使用路径导入图片
      im = Image.open(openPicturePath)
      #使用 byte 流导入图片
      # im = Image.open(io.BytesIO(b))
      # 转化到灰度图
      imgry = im.convert('L')
      # 保存图像
      imgry.save(savePicturePath)

def black_white(openPicturePath,savePicturePath):
      #转灰度
      im = Image.open(openPicturePath)
      imgry = im.convert('L')
      #二值化
      threshold = 140
      table = []
      for j in range(256):
            if j < threshold:
                  table.append(0)
            else:
                  table.append(1)
      out = imgry.point(table, '1')
      out.save(savePicturePath)

def get_file_content(filePath):#百度OCR调用的函数，不用管
    with open(filePath, 'rb') as fp:
        return fp.read()

def proc_picture(openPicturePath,savePicturePath):
      img = cv2.imread(openPicturePath, 0)
      median = cv2.medianBlur(img, 5)#中值滤波
      cv2.imwrite(savePicturePath,median)

def interference_line(openPicturePath):
      img = cv2.imread(openPicturePath, 0)
      h, w = img.shape[:2]
      # opencv矩阵点是反的
      # img[1,2] 1:图片的高度，2：图片的宽度
      for y in range(1, w - 1):
            for x in range(1, h - 1):
                  count = 0
                  if img[x, y - 1] > 245:
                    count = count + 1
                  if img[x, y + 1] > 245:
                    count = count + 1
                  if img[x - 1, y] > 245:
                    count = count + 1
                  if img[x + 1, y] > 245:
                    count = count + 1
                  if count > 2:
                    img[x, y] = 255         #判断一圈有多少白的，超过2，就转成白的。
      cv2.imwrite('44444.png',img)
      return img

#调用百度ocr API

#APP_ID = '18450760'
#API_KEY = '6d5C9RntTAE5zVPnDx1CCGZf'
#SECRET_KEY = 'TtseDhbyABljTXPwc7EzkoCNQtjaqlea'
def baidu_OCR(APP_ID,API_KEY,SECRET_KEY):
      aipOcr  = AipOcr(APP_ID, API_KEY, SECRET_KEY)

      # 读取图片
      filePath = "grey-2.jpg"

      # 定义参数变量
      options = {
        'probability':'true',
        'language_type': 'ENG',
      }

      # 调用通用文字识别接口
      result = aipOcr.basicAccurate(get_file_content(filePath), options)
      return result
