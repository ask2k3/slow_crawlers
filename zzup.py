import bs4, requests, time
import time
import progressbar

suffix1 = "page-"
file_path = "C:\\Users\\ykhan\\Downloads\\"
suffix2 = ".html"
num_of_pages = 2  # 81


def get_img_url(base_url):
    temp_url = []
    # file_name = file_path + "\\" + gallery_name + "-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    # file_handle = open(file_name, "a+")
    for page in progressbar.progressbar(range(10)):
        page = requests.get(base_url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        for link in soup.findAll('div', class_='picbox'):
            for a in link.find_all('a'):
                page = requests.get("https://archive.zzup.com/" + a.get('href'))
                time.sleep(16)
                soup = bs4.BeautifulSoup(page.content, "html.parser")
                print(soup)


    # file_handle.close()'''


def return_souped_content(url):
    page = requests.get(url)
    return bs4.BeautifulSoup(page.content, "html.parser")


def get_list_of_urls(raw_url):
    linked_urls = []
    for elx in progressbar.progressbar(range(num_of_pages)):
        rough_url = raw_url + suffix1 + str(elx + 1) + suffix2
        soup = return_souped_content(rough_url)
        for link in soup.findAll('div', class_='picbox'):
            for a in link.find_all('a'):
                if 'user-album' in a.get('href'):
                    continue
                else:
                    linked_urls.append("https://archive.zzup.com/" + a.get('href'))
    return linked_urls


if __name__ == '__main__':

    list_of_urls = "https://archive.zzup.com/search/milena/"

    gallery_title = [
        "55987-gabrielle-genevieve-haugh",
        "26346-katiusha-feofanova"
    ]

    all_urls = get_list_of_urls(list_of_urls)

    for el in all_urls:
        get_img_url(el)
