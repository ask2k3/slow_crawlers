import re, os, sys, glob
import bs4, requests
import time
import urllib.request
import progressbar
from selenium import webdriver
import aiohttp
import asyncio

url = "https://www.yaplakal.com/forum2/st/0/topic1879636.html"
base_url = "https://www.yaplakal.com/forum2/st/"
gallery_name = "topic1879636"
page_count = 482
file_path = "C:\\Users\\ykhan\\Downloads\\"


async def funny(current_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(current_url, headers=headers, verify_ssl=False) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            soup_content = await response.text()
            return soup_content

if __name__ == '__main__':
    playlist = []
    url_thread_number = re.split('/', url)[-1]
    for val in progressbar.progressbar(range(page_count)):
        detailed_url = base_url + str(val*25) + "/" + url_thread_number
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/76.0.3809.100 Safari/537.36'}
        html = ''
        loop = asyncio.get_event_loop()
        soup = loop.run_until_complete(funny(detailed_url))
        soup = bs4.BeautifulSoup(soup, features="html.parser")
        for link in soup.findAll('a', {'class': 'basic-img'}):
            playlist.append('https:' + link['href'])

    file_name = file_path + "\\" + url_thread_number + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a+")
    print("Finished parsing jpg files. Writing to file now ... ")
    for val in progressbar.progressbar(range(len(playlist))):
        file_handle.write(str(playlist[val]) + "\n")
    file_handle.close()
