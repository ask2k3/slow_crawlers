import bs4, requests
import time
import progressbar

#base_url = "https://motherless.com/gi/hot_teen_girls"
#gallery_name = "hot_teen_girls"
suffix = "?page="
cdn_url = "https://cdn5-images.motherlessmedia.com/images/"
#page_count = 1200
file_path = "C:\\Users\\ykhan\\Downloads\\"


def get_img_url(base_url, page_count, gallery_name):
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

    list_of_urls = [
        "https://motherless.com/GI03532E4",
        "https://motherless.com/GI2E2E87F",
        "https://motherless.com/G0188CC5",
        "https://motherless.com/GI2EDEB64",
        "https://motherless.com/gi/_daddy_s_perfect_little_toy_",
        "https://motherless.com/GI02E0D51"
    ]

    num_of_pages = [2, 49, 2, 220, 2388, 3]

    gallery_title = [
        "GI03532E4_Target genetic material for Cultured meat",
        "GI2E2E87F_Hot teen chicks",
        "G0188CC5_Extremely Cute and Incredibly Fuckable",
        "GI2EDEB64_Best of Motherless 2022 Summer",
        "daddy_s_perfect_little_toy",
        "GI02E0D51_perfect pussy"
    ]

    for el in range(len(list_of_urls)):
        print("Processing Gallery ... ", list_of_urls[el])
        get_img_url(list_of_urls[el], num_of_pages[el], gallery_title[el])