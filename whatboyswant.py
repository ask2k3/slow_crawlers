import bs4, requests, time
import time
import progressbar

suffix1 = "?page="
file_path = "C:\\Users\\ykhan\\Downloads\\"
# master_url = "https://whatboyswant.com/babes/party-babes"


def return_souped_content(url):
    page = requests.get(url)
    return bs4.BeautifulSoup(page.content, "html.parser")


def decode_master_url(current_url):
    split_url = current_url.split("=")
    num_of_pages = int(split_url[-1])
    gallery_name = current_url.split("/")[-1].split("?")[0]
    master_url = current_url.split("?")[0]
    all_img_urls = []
    for page in progressbar.progressbar(range(num_of_pages)):
        soup = return_souped_content(master_url + suffix1 + str(page + 1))
        for a in soup.find_all('a', href=True):
            if "?c=" in a['href']:
                all_img_urls.append(master_url[:24] + a['href'])
    return [ all_img_urls, gallery_name, master_url ]


def use_url_links_to_retrieve_img_url(info):
    gallery, img_urls, master_url = info[1], info[0], info[2]
    print("\n Processing images in url pages : ", master_url)
    file_name = file_path + "\\" + gallery + "-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    file_handle = open(file_name, "a+")
    for el in progressbar.progressbar(range(len(img_urls))):
        soup = return_souped_content(img_urls[el])
        images = [img['src'] for img in soup.find_all('img')]
        for i in images:
            if 'babes-norm' in i:
                file_handle.write(master_url[:24] + str(i + "\n"))
    file_handle.close()


if __name__ == '__main__':
    urllist = [
        # "https://whatboyswant.com/babes/non-nude-babes?page=9868",
        "https://whatboyswant.com/babes/lingerie-babes?page=6420",
        "https://whatboyswant.com/babes/candid-voyeur-creepshots?page=242",
        "https://whatboyswant.com/babes/see-thru-babe-pictures?page=543",
        "https://whatboyswant.com/babes/webcam-girls?page=642",
    ]

    for u in urllist:
        print("\n Processing url : ", u)
        use_url_links_to_retrieve_img_url(decode_master_url(u))
