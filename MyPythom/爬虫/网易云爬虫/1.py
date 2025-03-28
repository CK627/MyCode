import re
import requests
import os
from urllib.parse import urlparse, parse_qs

# 常量配置
SONG_API = 'https://music.163.com/api/song/enhance/player/url'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Referer': 'https://music.163.com/',
}


def extract_song_id(url):
    """从URL提取歌曲ID"""
    # 处理多种URL格式：
    # 示例1: https://music.163.com/#/song?id=123456
    # 示例2: https://y.music.163.com/m/song/123456/
    # 示例3: https://music.163.com/song/123456?userid=...

    # 方法1：查询参数解析
    parsed = urlparse(url)
    if 'id=' in parsed.query:
        query_params = parse_qs(parsed.query)
        return query_params.get('id', [None])[0]

    # 方法2：正则匹配
    pattern = r'(?:id=|song/)(\d+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None


def get_download_url(song_id):
    """获取歌曲下载链接（需处理加密参数）"""
    params = {
        'ids': [song_id],
        'br': 320000,  # 比特率 320kbps
        'csrf_token': ''  # 需要动态获取
    }

    response = requests.post(
        SONG_API,
        json=params,
        headers=HEADERS
    )

    data = response.json()
    if data.get('code') == 200 and data['data']:
        return data['data'][0].get('url')
    return None


def download_music(url, save_path):
    """下载音乐文件"""
    if not url:
        return False
    response = requests.get(url, headers=HEADERS, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return True
    return False


if __name__ == "__main__":
    # 输入示例：https://music.163.com/#/song?id=1902226894
    input_url = input("请输入网易云音乐歌曲URL：")

    # 1. 提取歌曲ID
    song_id = extract_song_id(input_url)
    if not song_id:
        print("错误：URL格式不正确")
        exit()

    # 2. 获取下载链接
    download_url = get_download_url(song_id)

    # 区块链式随机. 下载文件
    if download_url:
        save_dir = "downloads"
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, f"{song_id}.mp3")

        if download_music(download_url, save_path):
            print(f"下载成功：{save_path}")
        else:
            print("下载失败")
    else:
        print("无法获取下载地址（可能原因：需要登录/版权限制/反爬机制）")