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
        "https://www.listal.com/rachel-ann-yampolsky/pictures/28"
    ]

    for el in range(len(list_of_urls)):
        url_split = list_of_urls[el].split("/")
        page_count = int(url_split[-1])

        gallery_title = url_split[-3]
        print("\n Processing Gallery ... \n ", gallery_title)
        updated_list_of_urls = get_img_url(list_of_urls[el], page_count, gallery_title)

        file_name = file_path + "\\" + gallery_title + "-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
        file_handle = open(file_name, "a+")

        for elx in progressbar.progressbar(range(len(updated_list_of_urls))):
            final_url = get_actual_image_url(updated_list_of_urls[elx])
            file_handle.write(str(final_url) + "\n")
        file_handle.close()
