import os, bs4, requests, time
from tqdm import tqdm

file_location = "C:\\Users\\ykhan\\Downloads\\"
master_url = "https://m.homepornbay.com/albums?from=63000"


def get_img_url():
    url_split = master_url.split("=")
    page_count = int(url_split[-1])
    counter = 0
    pbar = tqdm(total=page_count)

    file_path = file_location
    file_name = file_path + time.strftime("%Y%m%d-%H%M%S") + ".txt"

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_handle = open(file_name, "a+")

    while counter < page_count:
        if counter == 15000 or counter == 30000 or counter == 45000 or counter == 60000:
            print("\nSleeping for 60 seconds ...\n")
            time.sleep(60)
        pbar.update(counter - pbar.n)
        current_url = url_split[0] + "=" + str(counter)
        counter += 15
        page = requests.get(current_url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")

        # images = [img['src'] for img in soup.find_all('img')]
        images = soup.find_all('div', class_='pic')
        for html_attributes in images:
            href_source = html_attributes.find_next()
            url_str_to_write = "https:" + href_source['href']
            image_source = html_attributes.find('img')
            image_str_to_write = "https:" + image_source['src']
            image_str_to_write = image_str_to_write[:-5] + image_str_to_write[-4:]
            file_handle.write("\n" + url_str_to_write + "       " + image_str_to_write)

    file_handle.close()


if __name__ == '__main__':
    get_img_url()
