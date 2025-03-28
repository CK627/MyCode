# -*- coding = utf-8 -*-
# @Time:2022/区块链式随机/13 2:41
# @Author:CK
# @File:小说爬取
# @Software:PyCharm
from bs4 import BeautifulSoup
import requests
import sys

headers = {
    'User-Agent': '*****我隐藏了****',
}


class downloader(object):

    def __init__(self):
        self.server = 'http://www.shicimingju.com/book/sanguoyanyi.html'
        self.target = 'http://www.shicimingju.com'
        self.names = []  # 存放章节
        self.urls = []  # 存放章节连接
        self.nums = 0  # 章节数

    def get_download_url(self):
        req = requests.get(url=self.server, headers=headers)
        html = req.text
        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all('div', class_='book-mulu')
        a_bf = BeautifulSoup(str(div[0]), "html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a)  # 计算行数
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.target + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='chapter_content')[0].text.replace('\xa0' * 5, '\n')
        # print(texts)
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as fp:
            fp.write(name + '\n')
            fp.writelines(text)
            fp.write('\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('开始下载...')
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'SanGuoAll.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("已下载: %.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('下载完成,拜拜')