import os
import threading
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from queue import Queue, Empty
import time


class FullSiteCrawler:
    def __init__(self, base_url, save_dir="downloaded_files", max_threads=4):
        self.base_url = base_url.rstrip('/') + '/'
        self.save_dir = os.path.abspath(save_dir)
        self.max_threads = max_threads
        self.queue = Queue()
        self.visited = set()
        self.lock = threading.Lock()
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; FullSiteCrawler/1.0)",
            "Accept-Encoding": "gzip, deflate"
        }
        self.queue.put(self.base_url)
        os.makedirs(self.save_dir, exist_ok=True)

    def _is_directory_listing(self, response):
        return 'text/html' in response.headers.get('Content-Type', '') and 'Index of /' in response.text

    def _convert_url_to_path(self, url):
        path = urlparse(url).path[len(urlparse(self.base_url).path):]
        clean_path = os.path.normpath(path).lstrip('/')
        return os.path.join(self.save_dir, clean_path)

    def worker(self):
        while True:
            try:
                url = self.queue.get(timeout=30)
                if url is None:
                    break

                with self.lock:
                    if url in self.visited:
                        continue
                    self.visited.add(url)

                self.process_url(url)
                self.queue.task_done()

            except Empty:
                break
            except Exception as e:
                print(f"Worker error: {str(e)}")

    def process_url(self, url):
        try:
            with self.session.get(url, headers=self.headers, stream=True, timeout=15) as response:
                response.raise_for_status()

                if self._is_directory_listing(response):
                    self.process_directory(url, response.text)
                else:
                    self.save_file(url, response)

        except Exception as e:
            print(f"Failed to process {url}: {str(e)}")

    def process_directory(self, url, html):
        """处理目录列表页面"""
        print(f"Processing directory: {url}")
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find_all('tr')[3:-1]

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
            absolute_url = urljoin(url, href)
            if absolute_url.endswith('/'):
                absolute_url = absolute_url.rstrip('/') + '/'

            with self.lock:
                if absolute_url not in self.visited:
                    self.queue.put(absolute_url)

    def save_file(self, url, response):
        if self._is_directory_listing(response):
            return

        save_path = self._convert_url_to_path(url)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        if os.path.exists(save_path):
            remote_size = int(response.headers.get('Content-Length', 0))
            local_size = os.path.getsize(save_path)
            if local_size == remote_size:
                print(f"File exists: {save_path}")
                return
        file_size = int(response.headers.get('Content-Length', 0))
        if file_size > 500 * 1024 * 1024:
            self._chunked_download(url, save_path, file_size)
        else:
            self._simple_download(response, save_path)

    def _chunked_download(self, url, save_path, total_size):
        temp_path = save_path + '.part'
        downloaded = 0
        if os.path.exists(temp_path):
            downloaded = os.path.getsize(temp_path)
            if downloaded >= total_size:
                os.rename(temp_path, save_path)
                return

        headers = self.headers.copy()
        headers['Range'] = f'bytes={downloaded}-'

        try:
            with self.session.get(url, headers=headers, stream=True, timeout=30) as response:
                response.raise_for_status()

                with open(temp_path, 'ab') as f:
                    for chunk in response.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            print(f"Downloading {os.path.basename(save_path)}: "
                                  f"{downloaded / 1024 / 1024:.1f}MB/{total_size / 1024 / 1024:.1f}MB")

            os.rename(temp_path, save_path)
            print(f"Saved: {save_path}")

        except Exception as e:
            print(f"Download failed: {save_path} - {str(e)}")
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def _simple_download(self, response, save_path):
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        print(f"Saved: {save_path}")

    def start(self):
        threads = []
        for i in range(self.max_threads):
            t = threading.Thread(target=self.worker, name=f"Worker-{i + 1}")
            t.start()
            threads.append(t)
        try:
            while not self.queue.empty():
                time.sleep(1)
            self.queue.join()
        except KeyboardInterrupt:
            print("\n用户中断，正在清理...")
        finally:
            for _ in range(self.max_threads):
                self.queue.put(None)
            for t in threads:
                t.join()


if __name__ == "__main__":
    CRAWLER = FullSiteCrawler(
        base_url="https://4b9d275e.r11.cpolar.top/",
        save_dir="1",
        max_threads=6
    )
    CRAWLER.start()