import bs4, requests
import time
import progressbar

file_path = "C:\\Users\\ykhan\\Downloads\\"


def get_img_url(base_url, page_count, gallery_name):
    unique_url_list = []
    for page in progressbar.progressbar(range(page_count)):
        url = base_url + "/" + str(page + 1)
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        for link in soup.findAll('a'):
            if 'viewimage' in link['href']:
                unique_url_list.append(link['href'])
    return unique_url_list


def get_actual_image_url(img_url):
    url_split = img_url.split("/")
    page = requests.get(img_url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    images = [img['src'] for img in soup.find_all('img')]
    for i in images:
        if str(url_split[-1]) in i:
            return i


if __name__ == '__main__':

    list_of_urls = [
        "https://www.listal.com/olivia-ponton/pictures"
    ]

    num_of_pages = [23]

    gallery_title = "olivia-ponton"

    for el in range(len(list_of_urls)):
        print("\n Processing Gallery ... \n ", list_of_urls[el])
        list_of_urls = get_img_url(list_of_urls[el], num_of_pages[el], gallery_title[el])

    file_name = file_path + "\\" + gallery_title + "-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a+")

    for el in progressbar.progressbar(range(len(list_of_urls))):
        final_url = get_actual_image_url(list_of_urls[el])
        file_handle.write(str(final_url) + "\n")
    file_handle.close()
