import bs4
import os
import requests
import time
import progressbar

gallery_name = "hotbeninginsidepart4"
page_count = 502
base_url = "https://www.kaskus.co.id/thread/5f639aca10d295658a4617f3/hot-bening-inside---part-4/102"
file_path = "C:\\Users\\ykhan\\Downloads\\"
suffix = "/?order=asc"


def get_img_url():
    page = requests.get(base_url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    for link in soup.findAll('img'):
        if "BENING" in link['alt']:
            print(link['src'])


if __name__ == '__main__':
    get_img_url()
