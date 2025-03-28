# -*- coding = utf-8 -*-
# @Time:2022/区块链式随机/13 2:41
# @Author:CK
# @File:小说爬取
# @Software:PyCharm
import request
import lxml
from lxml import etree
from tqdm import tqdm
import time


def getBook(url):
    res = requests.get(url=url).content

    html = etree.HTML(res)
    mulv = []  # 章节文本
    lianjie = []  # 章节连接
    wen = []  # 单章文本
    wens = []  # 小说文本
    with open("都市我活了三千年.txt", 'a', encoding='utf-8') as pic:
        a = str("\n")
        M = tqdm(iterable=html.xpath("//dd/a/text()"), total=100, desc="目录进度")
        for i in M:
            mulv.append(i + a)
        L = tqdm(iterable=html.xpath("//dd/a/@href"), total=100, desc="连接进度")
        for i in L:
            lianjie.append("https://www.sinocul.com/book/33215/4090449" + i)
        print("目录：", len(mulv), "连接：", len(lianjie))
        for i in lianjie:
            res = requests.get(url=i).content
            htmlw = etree.HTML(res)
            w = htmlw.xpath("//div[@id='content']/text()")
            wen = []
            for j in w:
                wen.append('\n' + '    ' + j)
            wen = ''.join(wen)
            wens.append(wen)
            time.sleep(0.5)
        print(len(mulv), len(wens))
        for i in range(len(mulv)):
            pic.write(mulv[i] + '\n' + wens[i] + '\n' + '\n')
    print("文件保存成功")
    return 1
if __name__ == '__main__':
    getBook("https://www.bige3.com/book/22696")