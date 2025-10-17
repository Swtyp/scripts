import os
import time

# SAMPLE

# PATH_URLS = r'C:\Users\User\Desktop\tmp\DNS\dns-urls.txt'


def new_tabs(urls_path: str, s: float):
    urls = []
    with open(urls_path, 'r', encoding='utf-8') as f:
        urls = f.readlines()
    for url in urls:
        os.system(f"firefox --new-tab {url}")
        time.sleep(s)


new_tabs(PATH_URLS, 1.5)