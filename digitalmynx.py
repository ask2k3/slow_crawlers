import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

site = "http://www.digitalminx.com"
base_url = "/celeb_pages/models/g/"
gallery_name = "georgieva_tatyana_"
suffix = ".htm"
cdn_url = "https://cdn5-images.motherlessmedia.com/images/"
page_count = 17
file_path = "C:\\Users\\ykhan\\Downloads\\"


def get_img_url():
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = file_path + "\\" + gallery_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a")

    for page in progressbar.progressbar(range(page_count+1)):
        if page < 9:
            url = site + base_url + gallery_name + str(0) + str(page+1) + suffix
        elif 10 <= page:
            url = site + base_url + gallery_name + str(page) + suffix

        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")

        for a in soup.find_all('a', href=True):
            if 'jpg' in a['href']:
                temp_img_url = a['href']
                img_url = site + temp_img_url[8:]
                file_handle.write(str(img_url) + "\n")

    file_handle.close()


if __name__ == '__main__':
    get_img_url()
