import requests
for x in range(1,255):
    url = "http://192.168.{}.2/".format(x)
    try:
        r = requests.post(url)
        print(url)
    except:
        pass
