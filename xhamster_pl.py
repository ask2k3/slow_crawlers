import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar

base_url = "https://xhamster.com/users/pmvcollection/videos/"
gallery_name = "GV8A005C9"
page_count = 7
file_path = "C:\\Users\\ykhan\\Downloads\\xhamster_pl"


def get_html_content(url):
    return bs4.BeautifulSoup(requests.get(url).content, "html.parser")


def get_mp4_url(playlist_url):
    playlist_soup = get_html_content(playlist_url)
    temp_mp4_links = [x['src'] for x in playlist_soup.find('video').find_all("source")]
    return temp_mp4_links[-1]


if __name__ == '__main__':
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    file_name = file_path + "\\" + gallery_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a+")

    for val in progressbar.progressbar(range(page_count)):
        detailed_url = base_url + str(val + 1)
        url_soup = get_html_content(detailed_url)
        for link in url_soup.findAll('a', {'class': 'video-thumb__image-container'}, href=True):
            file_handle.write(str(link['href']) + "\n")
    file_handle.close()
