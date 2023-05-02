import bs4, requests
import time
import progressbar

base_url = "https://motherless.com/gi/hot_teen_girls"
gallery_name = "hot_teen_girls"
suffix = "?page="
cdn_url = "https://cdn5-images.motherlessmedia.com/images/"
page_count = 1200
file_path = "C:\\Users\\ykhan\\Downloads\\"


def get_img_url():
    file_name = file_path + "\\" + gallery_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"

    file_handle = open(file_name, "a+")
    for page in progressbar.progressbar(range(page_count)):
        url = base_url + suffix + str(page + 1)
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        for link in soup.findAll('a', {'class': 'img-container'}):
            final_url = cdn_url + link['href'][-7:] + ".jpg"
            # print(final_url)
            file_handle.write(str(final_url) + "\n")

    file_handle.close()


if __name__ == '__main__':
    get_img_url()
