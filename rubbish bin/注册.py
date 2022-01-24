from PIL import Image
from aip import AipOcr

#截取验证码部分


img = Image.open("1.jpg")
cropped = img.crop((550, 281, 612, 304))  # (left, upper, right, lower) 左上，右下
Image._show(cropped)
cropped=cropped.convert('RGB')
cropped.save("2.jpg")

#使用路径导入图片
im = Image.open("2.jpg")
#使用 byte 流导入图片
# im = Image.open(io.BytesIO(b))
# 转化到灰度图
imgry = im.convert('L')
# 保存图像
imgry.save('gray-' + "2.jpg")

# 二值化，采用阈值分割法，threshold为分割点
threshold = 140
table = []
for j in range(256):
      if j < threshold:
            table.append(0)
      else:
            table.append(1)
out = imgry.point(table, '1')
out.save('b' + "2.jpg")

#调用百度ocr API
APP_ID = '18450760'
API_KEY = '6d5C9RntTAE5zVPnDx1CCGZf'
SECRET_KEY = 'TtseDhbyABljTXPwc7EzkoCNQtjaqlea'

aipOcr  = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "gray-2.jpg"
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
  'probability':'true',
  'language_type': 'ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicAccurate(get_file_content(filePath), options)

print(result)
