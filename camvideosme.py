# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

model_name = "mariabecky"
# base_url = "http://camgirlvideos.org/page/"
base_url = "http://camvideos.me/search/"
page_count = 12
file_location = "C:\\Users\\ykhan\\Downloads\\"
image_key = "th"


def get_img_url():
    image_url_list = []

    file_path = file_location + model_name
    file_name = file_path + "\\" + model_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for page in progressbar.progressbar(range(page_count)):
        url = base_url + model_name + "?page=" + str(page + 1)

        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        images = soup.findAll('img')

        for el in range(len(images)):
            if image_key in str(images[el]):
                temp_url = str(images[el])
                # left_index = 17 + len(model_name)
                temp_url = temp_url[10:-9] + "jpg"
                # temp_url = temp_url[0:7] + temp_url[9:]
                # print(temp_url)
            if "thro" in temp_url:
                temp_url = temp_url[16:]
                temp_url = "http://fastimages.org" + temp_url

            # print(temp_url)

            with open(file_name, "a") as file_handle:
                file_handle.write(str(temp_url) + "\n")
                file_handle.close()


if __name__ == '__main__':
    get_img_url()
