# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import bs4, requests
import time
import progressbar

page_count = 34
thread_id = "37473"
base_url = "https://xossipy.com/thread-"
url_suffix_1 = "-page-"
url_suffix_end = ".html"
file_location = "C:\\Users\\ykhan\\Downloads\\txt\\"


def get_html():
    file_path = file_location
    file_name = ""
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for page in progressbar.progressbar(range(page_count)):
        url = base_url + thread_id + url_suffix_1 + str(page + 1) + url_suffix_end
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        story_title = replace_special_characters(soup.title.string)
        if not file_name:
            file_name = file_path + thread_id + "_" + story_title + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
        result = soup.find_all("div", {"class": "post_body scaleimages"})

        try:
            with open(file_name, "a", encoding="utf-8") as file_handle:
                for res in result:
                    file_handle.write(str(res.text) + "\n")
        except OSError:
            print("Could not open/read file:", file_name)
    # wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

    # pdfkit.from_file(file_name, file_name_pdf, configuration=wkhtml_path)


def replace_special_characters(text):
    for ch in ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', '\'', '】', '/']:
        if ch in text:
            text = text.replace(ch, " ")
    return text


if __name__ == '__main__':
    get_html()
