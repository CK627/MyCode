#需要的模块
import re
import requests
#获取url_list,就是所有的图片链接
def get_url(url):
    response = requests.get(url)
    response.encoding='utf-8'
    url_addr = r'<img src="(.*?)" alt=".*?" border="0"/>'
    url_list = re.findall(url_addr,response.text)
 ##   print(url_list)
    return url_list
#下载保存所有的图片
def get_GIF(url,a):
    response = requests.get(url)
    with open("C:\\Users\\lenovo\\Pictures\\Saved Pictures\\%d.gif"%a,'wb') as file:
        file.write(response.content)
#程序开始
if __name__=='__main__':
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDYsMSw0LDIsNSw3LDgsOQ%3D%3D'
    url_list = get_url(url)
    zt=1
    for url in url_list:
        url = 'https://image.baidu.com'+url
        get_GIF(url, zt)
        zt+=1