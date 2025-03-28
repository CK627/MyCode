import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time

BASE_URL = "https://121d7635.r11.cpolar.top/"
SAVE_DIR = "downloaded_files"
DELAY = 0.1
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

visited_urls = set()
total_files = 0
total_errors = 0


def sanitize_filename(name: str) -> str:
    return "".join([c for c in name if c.isalnum() or c in ('.', '-', '_')]).strip()
def process_entity(parent_url: str, href: str, parent_local_path: str):
    global total_files, total_errors

    full_url = urljoin(parent_url, href)
    parsed = urlparse(full_url)
    base_name = sanitize_filename(os.path.basename(parsed.path.rstrip('/')) )
    if href.endswith('/'):
        dir_path = os.path.join(parent_local_path, base_name)
        os.makedirs(dir_path, exist_ok=True)

        try:
            process_directory(full_url, dir_path)
        except Exception as e:
            print(f"目录处理失败 {full_url}: {str(e)}")
            save_path = os.path.join(dir_path, f"{base_name}.html")
            download_file(full_url, save_path)
    else:
        file_name = sanitize_filename(os.path.basename(parsed.path))
        save_path = os.path.join(parent_local_path, file_name)
        time.sleep(DELAY)
        download_file(full_url, save_path)

def download_file(url: str, save_path: str):
    global total_files, total_errors
    try:
        if os.path.exists(save_path):
            return

        with requests.get(url, headers=HEADERS, stream=True, timeout=10) as r:
            r.raise_for_status()
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        total_files += 1
    except Exception as e:
        total_errors += 1
        if os.path.exists(save_path):
            os.remove(save_path)
        print(f"文件下载失败 {url}: {str(e)}")


def process_directory(url: str, local_path: str):
    if url in visited_urls:
        return
    visited_urls.add(url)

    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        for row in soup.select('table tr'):
            if len(row.find_all(['th', 'hr'])) > 0:
                continue
            link = row.select_one('td:nth-of-type(2) a')
            if not link or not link.get('href'):
                continue
            href = link.get('href')
            if href in ['../', './']:
                continue
            process_entity(url, href, local_path)
            time.sleep(DELAY)
    except Exception as e:
        print(f"目录解析失败 {url}: {str(e)}")

if __name__ == "__main__":
    os.makedirs(SAVE_DIR, exist_ok=True)
    base_path = os.path.join(SAVE_DIR, urlparse(BASE_URL).netloc)

    process_directory(BASE_URL, base_path)
    print(f"执行完成 | 成功: {total_files} | 失败: {total_errors}")