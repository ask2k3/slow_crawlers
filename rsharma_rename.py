# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re, os, sys, glob
import bs4
base_directory = "C:\\Users\\ykhan\\Downloads\\7009\\"


def getfilelist():
    os.chdir(base_directory)
    file_list = []
    for file in glob.glob("*"):
        file_list.append(base_directory + file)
    return(file_list)

def doarename(filelist):
    for file in filelist:
        with open(file, newline='', encoding='utf-8') as f:
            soup = bs4.BeautifulSoup(f, features="html.parser")
            for elm in soup.select("span[class^=sr-only]"):
                if 'Page' in elm.text:
                    xr = elm.get_text()[5:8]
                    if xr[2:3].isalpha():
                        xr = xr[0]
                xrnew = base_directory + xr + ".html"
                f.close()
                os.replace(file, xrnew)
                break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filelist = getfilelist()
    doarename(filelist)
