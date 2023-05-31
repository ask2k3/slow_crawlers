import os, os.path, shutil, re

path = "C:\\My Web Sites\\GI3031818\\cdn5-images.motherlessmedia.com\\images"
# path = "C:\\My Web Sites\\acacia-brinley"
parent_list = os.listdir(path)
for count3 in range(10):
    for count2 in range(10):
        for count in range(10):
            new_path = "C:\\Users\\ykhan\\Downloads\\bkup\\gall\\rachel-ann-yampolsky\\" + str(count3) + str(count2) + str(count) + "\\"
            images = [f for f in (os.listdir(path)[:99]) if '.jpg']
            if len(images) > 0:
                if not os.path.exists(new_path):
                    os.makedirs(new_path)

                for image in images:
                    new_file_path = new_path + image
                    filename = path + "\\" + image
                    shutil.move(filename, new_file_path)
