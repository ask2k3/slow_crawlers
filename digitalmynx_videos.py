import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

site = "http://www.digitalminx.com"
base_url = "/celeb_pages/models/g/"
gallery_name = "georgieva_tatyana_video"
suffix = ".htm"
page_count = 2
file_path = "C:\\Users\\ykhan\\Downloads\\"


def get_img_url():
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = file_path + "\\" + gallery_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a")

    url = site + base_url + gallery_name + suffix

    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")

    for a in soup.find_all('a', href=True):
        if 'mp4' in a['href']:
            temp_video_url = a['href']
            video_url = site + temp_video_url[8:]
            print(video_url)
            file_handle.write(str(video_url) + "\n")

    file_handle.close()


if __name__ == '__main__':
    get_img_url()
