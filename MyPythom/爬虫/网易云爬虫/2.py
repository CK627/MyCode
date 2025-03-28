import requests


headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

url="https://m804.music.126.net/20250305180850/5513659a3a2429706044845625974566/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/56614303522/e153/e634/bc5b/e69f138236da6168372e1d254f5ff6df.m4a?vuutv=3Xu9bSsIBt6/eEbd4kNr699IUur0h16ONJJNBN+rJmWMea8WVK2Krg44HO7AMnkkspWhyyJ4M3CtXPZk2O6GwSybcMCVkufzun9Ker17AR4=&authSecret=0000019565b0a53511ce0a30849f1a7e"
resource = requests.get(url=url,headers=headers)

with open("2.mp3","wb") as file:
    file.write(resource.content)