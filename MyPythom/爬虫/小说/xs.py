# -*- coding = utf-8 -*-
# @Time:2022/10/18 14:41
# @Author:CK
# @File:xs
# @Software:PyCharm
import requests
import re



class NoveLSpider:

    def __init__(self):
        self.session = requests.Session() # 下载器


    def get_novel(self, url): # 下载小说
        index_html = self.download(url,encodings="gbk") # 下载小说的首页面html
        # print(index_html)

        novel_chapter_infos = self.get_chapter_info(index_html) # 提取章节信息，url网址


    def download(self, url, encodings):
        requests = self.session.get(url)
        requests.encoding = encodings
        html = requests.text
        return html


    def get_chapter_info(self, index_html):
        div = re.findall(r'<a.*?</a>',index_html,re.S)
        print(div)


if __name__=="__main__":
    novel_url = "http://www.quannovel.com/read/617/"
    spider = NoveLSpider() # 实例化
    spider.get_novel(novel_url)

