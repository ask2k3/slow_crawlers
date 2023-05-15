import bs4, requests
import time
import progressbar

suffix1 = "/content/page/"
file_path = "C:\\Users\\ykhan\\Downloads\\"
suffix2 = "/?type=forums_topic_post"

def get_img_url(base_url, page_count, gallery_name):
    file_name = file_path + "\\" + gallery_name + "-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a+")
    for page in progressbar.progressbar(range(page_count)):
        url = base_url + suffix1 + str(page + 1) + suffix2
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        for link in soup.findAll('a', {'class': 'ipsAttachLink_image'}):
            file_handle.write(str(link['href']) + "\n")

    file_handle.close()



if __name__ == '__main__':

    list_of_urls = [
        "https://www.bellazon.com/main/topic/55987-gabrielle-genevieve-haugh/",
        "https://www.bellazon.com/main/topic/26346-katiusha-feofanova/"
    ]

    num_of_pages = [ 3, 6]

    gallery_title = [
        "55987-gabrielle-genevieve-haugh",
        "26346-katiusha-feofanova"
    ]

    for el in range(len(list_of_urls)):
        print("\n Processing Gallery ... \n ", list_of_urls[el])
        get_img_url(list_of_urls[el], num_of_pages[el], gallery_title[el])
