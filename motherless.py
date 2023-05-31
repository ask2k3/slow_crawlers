import bs4, requests
import time
import progressbar

# base_url = "https://motherless.com/gi/hot_teen_girls"
# gallery_name = "hot_teen_girls"
suffix = "?page="
cdn_url = "https://cdn5-images.motherlessmedia.com/images/"
# page_count = 1200
file_path = "C:\\Users\\ykhan\\Downloads\\"


def get_img_url(base_url):
    url_split = base_url.split("=")
    page_count = int(url_split[-1])
    gallery_name = str(base_url.split("/")[-1]).split("?")[0]
    # gallery_name = base_url[23:] + " " + gallery_name
    file_name = file_path + "\\" + gallery_name + "-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"

    file_handle = open(file_name, "a+")
    for page in progressbar.progressbar(range(page_count)):
        url = str(url_split[0]) + "=" + str(page + 1)
        # print("\n", url)
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        for link in soup.findAll('a', {'class': 'img-container'}):
            final_url = cdn_url + link['href'][-7:] + ".jpg"
            file_handle.write(str(final_url) + "\n")

    file_handle.close()


if __name__ == '__main__':

    list_of_urls = [
        "https://motherless.com/gi/awesome_galleries_ect_of_teens__18__?page=2838",
        "https://motherless.com/gi/__several_porn_____?page=13763"
    ]

    for el in range(len(list_of_urls)):
        print("Processing Gallery ... ", list_of_urls[el])
        get_img_url(list_of_urls[el])
