import bs4, requests, os, time
import progressbar

index_count = 62
base_url = "https://xossipy.com/forum-17-page-"
url_suffix_1 = "-page-"
url_suffix_end = ".html?sortby=views"
file_location = "C:\\Users\\ykhan\\Downloads\\htmltext\\"

html_dict = {}
story_url = "https://xossipy.com/thread-"
story_url_suffix_1 = "-page-"
story_url_suffix_end = ".html"


def get_html(htm):
    file_path = file_location
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for thread_id, page_count in htm.items():
        file_name = ""
        '''if htm[items]:
            thread_id = htm[items][0]
            page_count = htm[items][1]'''

            #if is_integer(page_count) and thread_id:
        print("\n Processing Title# " + thread_id + "  ")
        for page in progressbar.progressbar(range(int(page_count))):
            url = story_url + thread_id + story_url_suffix_1 + str(page + 1) + story_url_suffix_end
            page = requests.get(url)
            soup = bs4.BeautifulSoup(page.content, "html.parser")
            story_title = replace_special_characters(soup.title.string)

            if not file_name:
                file_name = file_path + thread_id + "_" + story_title + "_" + ".txt "

            result = soup.find_all("div", {"class": "post_body scaleimages"})

            try:
                with open(file_name, "a+", encoding="utf-8") as file_handle:
                    for res in result:
                        file_handle.write(str(res.text) + "\n")
            except OSError:
                print("Could not open/read file:", file_name)

                file_handle.close()


def get_list_with_pages():
    file_name = ""

    for page in progressbar.progressbar(range(index_count)):
        url = base_url + str(page + 1) + url_suffix_end
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")

        spans = soup.find_all('span', "smalltext")
        for span in spans:
            links = span.find_all('a')
            thread_id_number, page_size = [], []
            for link in links:
                page_size.append(link.contents[-1])
                if 'thread' in link['href']:
                    thread_id_number = link['href'].split("-")[1]
                    thread_id_number = thread_id_number.split(".")[0]
                if thread_id_number and 10 >= len(page_size) >= 3:
                    html_dict[thread_id_number] = page_size[len(page_size)-1]

                    #html_dict.append([thread_id_number, page_size[len(page_size)-1]])

    file_path = file_location
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    if not file_name:
        file_name = file_path + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt "

    with open(file_name, "a+", encoding="utf-8") as file_handle:
        for res in html_dict:
            file_handle.write(str(res) + "\n")
    file_handle.close()
    print(len(html_dict))
    return html_dict


def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def replace_special_characters(text):
    for ch in ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', '\'', '】', '/',
               '~', '?']:
        if ch in text:
            text = text.replace(ch, " ")
    return text


if __name__ == '__main__':
    get_html(get_list_with_pages())
    #get_list_with_pages()
