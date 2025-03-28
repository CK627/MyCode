# -*- coding = utf-8 -*-
# @Time:2022/5/7 上午 1:40
# @Author:CK
# @File:bilibili
# @Software:PyCharm
import requests
if __name__ == '__main__':
    # url的确认
    url_30080 = 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/56/44/363734456/363734456_nb2-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632538815&gen=playurlv2&os=coso1bv&oi=1971857656&trid=9ff0468d9c8d4bc3bc3ea78a2dba6159u&platform=pc&upsig=ce82714ab55b6da3a6c523ec84738eb3&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=1331613198&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000'
    url_30280 = 'https://upos-sz-mirrorks3o1.bilivideo.com/upgcxcode/56/44/363734456/363734456_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632538815&gen=playurlv2&os=ks3o1bv&oi=1971857656&trid=9ff0468d9c8d4bc3bc3ea78a2dba6159u&platform=pc&upsig=7b16f7f39b708baa5a7ecfb49ece41a9&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=1331613198&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000'
    # 构造请求头信息
    headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Referer': 'https://www.bilibili.com/'
    }
    # 发送请求,获取响应
    response_30080 = requests.get(url_30080, headers=headers_)
    response_30280 = requests.get(url_30280, headers=headers_)
    # 提取数据,字节类型（content是字节类型，一般是视频，音频。text是文本类型，一般用来爬取文字，小说）
    data_30080 = response_30080.content
    data_30280 = response_30280.content
    # 保存
    with open('30080.mp4', 'wb') as f:
        f.write(data_30080)
    with open('30280.mp3', 'wb') as f:
        f.write(data_30280)