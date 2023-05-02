# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

model_name = "playwithmil"
base_url = "https://www.xvideos.com/channels/porn_force#_tabVideos"
page_count = 10
file_location = "C:\\Users\\ykhan\\PycharmProjects\\"
image_key = "fastimages"


def get_url():
    page = requests.get(base_url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    print(soup)



def file_transfer(img_url_list):
    file_path = file_location + model_name
    file_name = file_path + "\\" + model_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for img in progressbar.progressbar(range(len(img_url_list))):
        temp_url = img_url_list[img]
        new_file_name = file_path + "\\" + temp_url[40:]
        try:
            urllib.request.urlretrieve(temp_url, new_file_name)
        except Exception as e:
            print(e, "  ", temp_url, "  ",  img_url_list[img])
            continue

        with open(file_name, "a") as file_handle:
            file_handle.write(temp_url + "\n")
        file_handle.close()


if __name__ == '__main__':
    get_url()
    #file_transfer(img_list)
