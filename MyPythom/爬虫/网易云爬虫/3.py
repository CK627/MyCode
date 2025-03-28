import requests
from lxml import etree

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

singer_url = input(":")
url = singer_url.replace("/#","")
resource = requests.get(url=url,headers=headers)

html = etree.HTML(resource.text)
music_lable_list = html.xpath('//a[contains(@href,"/song?")]')

for music_lable in music_lable_list:
    href = music_lable.xpath('./@href')[0]
    music_id = href.split('=')[1]
    music_name = music_lable.xpath('./text()')[0]

    music_url = "http://music.163.com/song/media/outer/url?id" + music_id
    music = requests.get(music_url,headers=headers)

    try:
        with open('./music/%s.mp3' %music_name,"wb") as file:
            file.write(music.content)
        print('《%s》下载成功'%music_name)
    except:
        break