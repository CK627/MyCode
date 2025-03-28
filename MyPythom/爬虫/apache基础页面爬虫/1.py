import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote

def get_clean_path(url):
    parsed = urlparse(url)
    path = parsed.path.rstrip('/')
    if not path:
        return f"{parsed.scheme}://{parsed.netloc}:"
    return f"{path}/".replace('//', '/').lstrip('/')

def crawl_apache_directory(base_url):
    visited = set()
    queue = [base_url]

    with open("url.txt", "w", encoding="utf-8") as f:
        while queue:
            current_url = queue.pop(0)
            if current_url in visited:
                continue
            visited.add(current_url)

            try:
                response = requests.get(current_url, timeout=10)
                response.raise_for_status()
            except Exception as e:
                print(f"Error fetching {current_url}: {str(e)}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            entries = []
            dirs = []

            for row in soup.select('tr'):
                if row.find('th') or row.find('hr'):
                    continue

                img = row.find('img')
                a_tag = row.find('a')
                if not img or not a_tag:
                    continue

                # 处理目录/文件信息
                href = a_tag.get('href', '')
                href = href.split('?')[0]
                decoded = unquote(href)

                is_dir = 'folder.gif' in img.get('src', '')
                absolute_url = urljoin(current_url, href)

                if is_dir:
                    if not decoded.endswith('/'):
                        decoded += '/'
                    dirs.append(absolute_url)
                    entries.append(decoded)
                else:
                    entries.append(decoded.split('/')[-1])

            # 写入当前目录信息
            display_path = get_clean_path(current_url)
            f.write(f"{display_path}:\n")
            for entry in entries:
                f.write(f"{entry}\n")
            f.write("\n")

            # 添加子目录到队列
            queue.extend(dirs)

if __name__ == "__main__":
    target_url = "https://22092c2.r11.cpolar.top/"
    crawl_apache_directory(target_url)