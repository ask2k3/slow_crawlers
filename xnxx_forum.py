import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

site = "https://forum.xnxx.com/threads/"
gallery_name = "amazing-tits-and-assets-for-all.577609"
suffix = "/page-"
cdn_url = "https://cdn5-images.motherlessmedia.com/images/"
page_count = 193
file_path = "C:\\Users\\ykhan\\Downloads\\"


def get_img_url():
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = file_path + "\\" + gallery_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a", encoding="utf-8")

    for page in progressbar.progressbar(range(page_count+1)):
        url = site + gallery_name + suffix + str(page+1)

        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")

        images = [img['src'] for img in soup.find_all('img')]
        for image in images:
            if 'xnxx' in image and not 'avatar' in image:
                file_handle.write(str(image) + "\n")

    file_handle.close()


if __name__ == '__main__':
    get_img_url()
