import re
import time

import bs4
import pdfkit
import requests
import progressbar
counter = 10
base_url = "https://www.literotica.com/s/blood-love-ch-"
suffix = "?page="


def get_story(url):
    title = base_url[29:-4]
    file_name_html = "C:\\Users\\ykhan\\Downloads\\" + str(title) + ".html"
    file_name_pdf = "C:\\Users\\ykhan\\Downloads\\" + str(title) + ".pdf"
    headers = requests.utils.default_headers()
    is_title_written = 0
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    for page in progressbar.progressbar(range(100)):
        current_url = url + suffix + str(page + 1)
        content = requests.get(current_url, headers=headers)
        soup = bs4.BeautifulSoup(content.content, "html.parser")

        text_content = str(soup.find("div", class_="aa_ht"))
        if text_content == "None":
            break
            # story = [p.get_text() for p in text_content]

        with open(file_name_html, "a+", encoding='utf-8') as file:
            if is_title_written == 0:
                is_title_written = 1
                file.write("<div style = \"display:block; clear:both; page-break-after:always;\"></div>")
                file.write("<b style=\"font-size:25px;\" font face=\"Cascadia\" size=\"2\" color = \"black\"> ")
                file.write(url[29:].upper())
                file.write("</b>")
            if text_content != "None":
                file.write("<p style=\"font-family:Courier\">")
                file.write(text_content)
                file.write("</p>")

    options = {
        'dpi': 200,
        'page-size': 'A4',
        'disable-smart-shrinking': '',
    }
    pdfkit.from_url(file_name_html, file_name_pdf, options=options)


if __name__ == '__main__':
    for req in range(counter):
        if req < 10:
            default_val = "0" + str(req+1)
        else:
            default_val = str(req+1)
        print(" \n Processing ...  " + base_url + default_val)
        get_story(base_url + default_val)
