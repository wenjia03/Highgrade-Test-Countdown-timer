import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import requests
import json
import time
import os
import ctypes
import urllib.request
import os.path


def save_img(img_url,dirname):
    #保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        #获得图片文件名，包括后缀
        basename = 'in.jpg'
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    print("Save", filepath, "successfully!")

    return filepath

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)       
    img_url = r.url # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url
def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)

print("Designed By Wenjia Chen Copyright 2012 -2020")
print("Visit NEZHA.SPACE Opensource on Github @wenjia03")
print("Opensource on Github @wenjia03")
print('正在请求必应每日一图……')
dirname = "D:\\"       # 图片要被保存在的位置
img_url = get_img_url()
filepath = save_img(img_url, dirname)   # 图片文件的的路径
set_img_as_wallpaper(filepath)
apploc ='D:'
now = time.time()
endunix = 1623081600
re =  int((endunix -int(now) )/86400) + 1

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
print(str(apploc) + "\\in.jpg")
print("正在准备请求Hitokoto API……")
bk_img = cv2.imread(str(apploc) + "\\in.jpg")
#设置需要显示的字体
fontpath = "ziti.ttf"
font = ImageFont.truetype(fontpath, 48)
font3 = ImageFont.truetype(fontpath, 40)
font2 = ImageFont.truetype(fontpath,112)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
postmes = {'c' : 'i','max_length':16 }
rre = requests.get('https://v1.hitokoto.cn/',headers= headers ,params = postmes)
print("正在生成图片……")
rep = rre.json()
text = rep['hitokoto']
info ="——《"+str(rep['from'])+"》  " +str(rep['from_who'])
#绘制文字信息
draw.text((850 , 350),  "距离高考还有", font = font, fill = (255, 255, 255))
draw.text((850 , 400),  str(re) + "天", font = font2, fill = '#0000ff')
draw.text((650 , 530),  text, font = font, fill = (255, 255, 255))
draw.text((875 , 590),  info, font = font3, fill = (255, 255, 255))
bk_img = np.array(img_pil)
#cv2.imshow('test',bk_img)
#cv2.waitKey()
cv2.imwrite(str(apploc)+"\\out.jpg",bk_img)
set_img_as_wallpaper(str(apploc)+"\\out.jpg")
#designed by WenjiaChen on NEZHA.SPACE
#Visit more infomation in NEZHA.SPACE
#