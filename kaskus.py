import bs4
import os
import requests
import time
import progressbar
gallery_name = "hotbeninginsidepart4"
page_count = 502
base_url = "https://www.kaskus.co.id/thread/5f639aca10d295658a4617f3/hot-bening-inside---part-4/"
file_path = "C:\\Users\\ykhan\\Downloads\\"
suffix = "/?order=asc"


def get_img_url():
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = file_path + "\\" + gallery_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a+")

    for page in progressbar.progressbar(range(page_count+1)):
        url = base_url + str(page+1)
        print("\n" + url)
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        try:
            for link in soup.findAll('img'):
                if "BENING" in link['alt']:
                    if 'png' in link['src']:
                        file_handle.write(str(link['src']) + "\n")
        except KeyError:
            print(KeyError)

    file_handle.close()


if __name__ == '__main__':
    get_img_url()
