#第三方库
from urllib.request import urlretrieve#通过图片的地址下载图片
urlretrieve('https://www.bilibili.com/video/BV1vf4y1U7v4?t=55.8','撒野.mp4')
print('爬取成功！')