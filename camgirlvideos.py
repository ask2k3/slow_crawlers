# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

model_name = "playwithmil"
base_url = "http://camgirlvideos.org/page/"
page_count = 10
file_location = "C:\\Users\\ykhan\\PycharmProjects\\"
image_key = "fastimages"


def get_img_url():
    image_url_list = []

    for page in progressbar.progressbar(range(page_count)):
        url = base_url + str(page + 1) + "/?s=" + model_name

        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        images = soup.findAll('img')

        for el in range(len(images)):
            if image_key in str(images[el]):
                temp_url = str(images[el])
                left_index = 17 + len(model_name)
                temp_url = temp_url[left_index:-9] + "jpg"
                #temp_url = temp_url[0:7] + temp_url[9:]
                image_url_list.append(temp_url)

    return image_url_list


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
    img_list = get_img_url()
    file_transfer(img_list)
