import requests
import os
from lxml import etree


def create_file(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

url = 'https://wk.baidu.com/view/526297e64531b90d6c85ec3a87c24028905f8521'

resp = requests.get(url)
text = resp.text

html = etree.HTML(text)

img_list = html.xpath('//div[@class="mod flow-ppt-mod"]/div/div/img')
cnt = 1
file_path = './wendang/'
create_file(file_path)
for i in img_list:
    try:
        img_url = i.xpath('./@src')[0]
    except:
        img_url = i.xpath('./@data-src')[0]
    file_name = f'{file_path}page_{cnt}.jpg'
    print(file_name, img_url)
    resp = requests.get(img_url)
    with open(file_name, 'wb') as f:
        f.write(resp.content)

    cnt += 1