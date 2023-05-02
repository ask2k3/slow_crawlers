# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

file_location = "C:\\Users\\ykhan\\Downloads\\"
urls = ["https://m.homepornbay.com/album/sexy-german-teen-gf-anna",
        "https://m.homepornbay.com/album/young-amateur-girl-posing-for-boyfriend2",
        "https://m.homepornbay.com/album/teenage-amateur-girl-hot-selfies",
        "https://m.homepornbay.com/album/teenage-amateur-gf-nude-selfies-collection",
        "https://m.homepornbay.com/album/dirty-college-cheerleader-katelyn",
        "https://m.homepornbay.com/album/young-amateur-couple-private-pics-collection7",
        "https://m.homepornbay.com/album/teen-whore-athenas-selfies",
        "https://m.homepornbay.com/album/skinny-tiny-tit-teen-gf-allison",
        "https://m.homepornbay.com/album/teen-amateur-gf-nude-posing-and-cock-sucking2",
        "https://m.homepornbay.com/album/blonde-teen-babe-alone-and-with-friend",
        "https://m.homepornbay.com/album/teenage-amateur-gf-exposed9",
        "https://m.homepornbay.com/album/young-amateur-gf-homemade-pics-collection3",
        "https://m.homepornbay.com/album/young-n-hot-teen-gf",
        "https://m.homepornbay.com/album/sexy-young-amateur-babe4",
        "https://m.homepornbay.com/album/pretty-amateur-gf-nn-pics",
        "https://m.homepornbay.com/album/petite-teen-gf-nude-selfies",
        "https://m.homepornbay.com/album/young-amateur-blonde-gf-homemade-pics-collection2",
        "https://m.homepornbay.com/album/skinny-blond-slut-love-fucking",
        "https://m.homepornbay.com/album/never-enough-of-this-amazing-goddes",
        "https://m.homepornbay.com/album/amateur-gf-making-hot-selfies2",
        "https://m.homepornbay.com/album/young-blonde-babe-making-selfies",
        "https://m.homepornbay.com/album/amateur-couple-share-homemade-porn87",
        "https://m.homepornbay.com/album/WhiteWine",
        "https://m.homepornbay.com/album/sexy-skinny-flat-tit-teen-gf-kylie",
        "https://m.homepornbay.com/album/teasing-teen-gf-nude-mirror-selfies",
        "https://m.homepornbay.com/album/nude-petite-amateur-girl",
        "https://m.homepornbay.com/album/family-sex-mix-1",
        "https://m.homepornbay.com/album/super-cute-blonde-babe2",
        "https://m.homepornbay.com/album/pretty-young-amateur-gf5",
        "https://m.homepornbay.com/album/young-amateur-blond-camwhore"
        ]

img_list = []

def get_img_url(url_parameter):
    image_url_list = []

    page = requests.get(url_parameter)
    soup = bs4.BeautifulSoup(page.content, "html.parser")

    images = [img['src'] for img in soup.find_all('img')]
    cnt = 0
    for elx in range(len(images)):
        if cnt == 0:
            el = images[elx]
            el = "http:" + el[:-5] + ".jpg"
            image_url_list.append(el)
            cnt = 1
        else:
            cnt = 0
    return image_url_list


def file_transfer(img_url_list):
    file_path = file_location
    file_name = file_path + time.strftime("%Y%m%d-%H%M%S") + ".txt"

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_handle = open(file_name, "a+")

    for img in progressbar.progressbar(range(len(img_url_list))):
        file_handle.write(str(img_url_list[img]) + "\n")

    file_handle.close()


if __name__ == '__main__':
    for url in urls:
        img_list.append(get_img_url(url))
    flat_list = [item for sublist in img_list for item in sublist]
    file_transfer(flat_list)

