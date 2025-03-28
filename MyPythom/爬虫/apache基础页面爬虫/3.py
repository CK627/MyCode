import os
import threading
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from queue import Queue, Empty
import time


class FixedPathSiteCrawler:
    def __init__(self, base_url, save_dir="download", max_threads=4):
        self.base_url = base_url
        self.save_dir = save_dir
        self.max_threads = max_threads

        # 确保base_url以/结尾
        if not self.base_url.endswith('/'):
            self.base_url += '/'

        self.queue = Queue()
        self.visited = set()
        self.lock = threading.Lock()
        self.session = requests.Session()

        # 创建根保存目录
        os.makedirs(self.save_dir, exist_ok=True)

        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; FileCrawler/3.0)",
            "Accept-Encoding": "gzip, deflate"
        }

    def _get_local_path(self, url):
        """将URL转换为本地保存路径，保留完整目录结构"""
        parsed = urlparse(url)

        # 提取相对于base_url的路径部分
        base_parsed = urlparse(self.base_url)
        relative_path = parsed.path[len(base_parsed.path):]

        # 处理路径中的../等特殊情况
        clean_path = os.path.normpath(relative_path).lstrip('/')

        # 构建完整保存路径
        full_path = os.path.join(self.save_dir, clean_path)

        # 如果是目录则添加index.html
        if url.endswith('/'):
            full_path = os.path.join(full_path, 'index.html')

        return full_path

    def worker(self):
        while True:
            try:
                url = self.queue.get(timeout=30)
                if url is None:
                    break

                self.process_url(url)
                self.queue.task_done()
            except Empty:
                break
            except Exception as e:
                print(f"Worker error: {str(e)}")

    def process_url(self, url):
        with self.lock:
            if url in self.visited:
                return
            self.visited.add(url)

        print(f"Processing: {url}")

        try:
            # HEAD请求判断资源类型
            head_resp = self.session.head(url, headers=self.headers, timeout=10)

            if 'text/html' in head_resp.headers.get('Content-Type', ''):
                self.process_directory(url)
            else:
                self.download_file(url)
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")

    def process_directory(self, url):
        try:
            resp = self.session.get(url, headers=self.headers, timeout=15)
            resp.raise_for_status()

            # 保存目录索引文件
            save_path = self._get_local_path(url)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(resp.content)
            print(f"Saved directory index: {save_path}")

            # 解析子目录和文件
            self.parse_links(resp.text, url)
        except Exception as e:
            print(f"Directory process failed: {url} - {str(e)}")

    def parse_links(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find_all('tr')[2:-1]

        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 3:
                continue

            link = cols[1].find('a')
            if not link:
                continue

            href = link.get('href')
            if href in ('../', './'):
                continue

            absolute_url = urljoin(base_url, href)

            with self.lock:
                if absolute_url not in self.visited:
                    self.queue.put(absolute_url)

    def download_file(self, url):
        save_path = self._get_local_path(url)
        temp_path = save_path + '.part'

        # 检查文件是否已存在
        if os.path.exists(save_path):
            print(f"File already exists: {save_path}")
            return

        # 创建父目录
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        try:
            with self.session.get(url, stream=True, timeout=30) as resp:
                resp.raise_for_status()

                # 获取文件大小
                total_size = int(resp.headers.get('Content-Length', 0))

                # 分块下载大文件（500MB以上）
                if total_size > 500 * 1024 * 1024:
                    self._chunked_download(resp, temp_path, save_path, total_size)
                else:
                    self._simple_download(resp, temp_path, save_path)

        except Exception as e:
            print(f"Download failed: {url} - {str(e)}")
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def _chunked_download(self, response, temp_path, save_path, total_size):
        downloaded = 0
        if os.path.exists(temp_path):
            downloaded = os.path.getsize(temp_path)

        headers = self.headers.copy()
        headers['Range'] = f'bytes={downloaded}-'

        with open(temp_path, 'ab') as f:
            with self.session.get(response.url, headers=headers, stream=True) as resp:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        print(
                            f"Downloading {save_path}: {downloaded / 1024 / 1024:.1f}MB/{total_size / 1024 / 1024:.1f}MB")

        os.rename(temp_path, save_path)
        print(f"Saved large file: {save_path}")

    def _simple_download(self, response, temp_path, save_path):
        with open(temp_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        os.rename(temp_path, save_path)
        print(f"Saved file: {save_path}")

    def start(self):
        self.queue.put(self.base_url)

        # 启动工作线程
        threads = []
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        # 等待任务完成
        self.queue.join()

        # 清理线程
        for _ in range(self.max_threads):
            self.queue.put(None)

        for t in threads:
            t.join()


if __name__ == "__main__":
    # 配置示例
    crawler = FixedPathSiteCrawler(
        base_url="https://4b9d275e.r11.cpolar.top/",
        save_dir="downloaded_files",
        max_threads=8
    )
    crawler.start()