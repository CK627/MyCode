import time
import requests
import pandas as pd
from datetime import datetime

url = "https://kyfw.12306.cn/otn/userCommon/allProvince"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

content_json = requests.get(url=url, headers=headers).json()
print("等待3s")
time.sleep(3)
print(content_json)
content_list = pd.json_normalize(content_json['data'], errors='ignore')

if __name__ == '__main__':
    curr_time = datetime.now()
    timestamp = datetime.strftime(curr_time, '%Y-%m-%d %H-%M-%S')
    content_list.to_excel(f"全国火车票代售点的省-{timestamp}.xlsx", index=False)
    print("保存完成！")
    rows = content_list.shape
    print("请求得到的表格行数与列数：", rows)