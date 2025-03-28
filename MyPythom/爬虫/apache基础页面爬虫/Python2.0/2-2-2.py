import os
import threading
import requests
from urlparse import urljoin, urlparse
from Queue import Queue, Empty
from bs4 import BeautifulSoup

class SiteCrawler:
    def __init__(self, base_url, save_dir="2", max_threads=4):
        self.base_url = base_url.rstrip('/') + '/'
        self.save_dir = os.path.abspath(save_dir)
        self.max_threads = max_threads
        self.queue = Queue()
        self.visited = set()
        self.lock = threading.Lock()
        self.session = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.queue.put(self.base_url)
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def _get_path(self, url):
        parsed = urlparse(url)
        base_path = urlparse(self.base_url).path
        rel_path = parsed.path[len(base_path):].lstrip('/')
        return os.path.join(self.save_dir, rel_path)

    def worker(self):
        while True:
            try:
                url = self.queue.get(timeout=10)
                if url in self.visited:
                    continue
                with self.lock:
                    self.visited.add(url)
                self._process(url)
                self.queue.task_done()
            except Empty:
                break
            except:
                pass

    def _process(self, url):
        try:
            resp = self.session.get(url, stream=True, timeout=15, headers=self.headers)
            if resp.status_code != 200:
                return

            if 'text/html' in resp.headers.get('content-type', '') and 'Index of /' in resp.text:
                self._parse_dir(url, resp.text)
            else:
                self._save_file(url, resp)
        except:
            pass

    def _parse_dir(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for row in soup.find_all('tr')[3:-1]:
            cols = row.find_all('td')
            if len(cols) < 3:
                continue
            link = cols[1].find('a')
            if not link:
                continue
            href = link.get('href')
            if href in ('../', './'):
                continue
            abs_url = urljoin(url, href)
            if abs_url not in self.visited:
                self.queue.put(abs_url)

    def _save_file(self, url, response):
        save_path = self._get_path(url)
        if os.path.exists(save_path):
            return
        dir_path = os.path.dirname(save_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        try:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024*1024):
                    if chunk:
                        f.write(chunk)
        except:
            if os.path.exists(save_path):
                os.remove(save_path)

    def start(self):
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
        self.queue.join()

if __name__ == "__main__":
    crawler = SiteCrawler(
        base_url="https://4b9d275e.r11.cpolar.top/",
        max_threads=6
    )
    crawler.start()