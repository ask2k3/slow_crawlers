import re, os, sys, glob
import bs4

base_directory = "C:\\Users\\ykhan\\Downloads\\bkup\\gall\\amazing-tits-and-assets-for-all.577609\\forum.xnxx.com\\attachments"
new_directory = "C:\\Users\\ykhan\\Downloads\\bkup\\gall\\amazing-tits-and-assets-for-all.577609\\forum.xnxx.com\\newdir"

c = 0
for root, dirs, files in os.walk(base_directory, topdown=False):
    folder_name = root[101:]
    for name in files:
        '''new_name = ""
        try:
            if 'jpeg' in folder_name or 'jpg' in folder_name:
                new_name = folder_name + '.jpg'
            if 'png' in folder_name:
                new_name = folder_name + '.png'
            if 'bmp' in folder_name:
                new_name = folder_name + '.bmp'
            if 'gif' in folder_name:
                new_name = folder_name + '.gif'

            if new_name != "":
            os.rename(os.path.join(root, name), os.path.join(root, new_name))
            # print("Renaming ", name, "to", new_name)'''

        os.replace(os.path.join(root, name), os.path.join(new_directory, name))
        # print('Moving from', os.path.join(root, new_name), ' to ' , os.path.join(new_directory, new_name))

        os.rmdir(root)

        '''except FileNotFoundError as e:
            print(str(e))'''
