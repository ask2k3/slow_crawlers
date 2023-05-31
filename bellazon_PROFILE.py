import bs4, requests
import time
import progressbar

suffix1 = "https://www.bellazon.com/main/profile/"
file_path = "C:\\Users\\ykhan\\Downloads\\"
suffix2 = "/content/page/"
suffix3 = "?type=forums_topic_post"

def get_img_url(base_url):  # , page_count, gallery_name):

    url_split = base_url.split("/")
    page_count = int(url_split[-2])

    # gallery_name = url_split[-4]
    gallery_name = url_split[-5]

    file_name = file_path + "\\" + gallery_name + "-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a+")
    for page in progressbar.progressbar(range(page_count)):
        url = suffix1 + gallery_name + suffix2 + str(page + 1) + suffix3
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        for link in soup.findAll('a', {'class': 'ipsAttachLink_image'}):
            file_handle.write(str(link['href']) + "\n")

    file_handle.close()


if __name__ == '__main__':

    list_of_urls = [
        "https://www.bellazon.com/main/profile/15092-alpat/content/page/431/?type=forums_topic_post"
    ]

    for el in range(len(list_of_urls)):
        print("\n Processing Gallery ... \n ", list_of_urls[el])
        get_img_url(list_of_urls[el])  # , num_of_pages[el], gallery_title[el])
