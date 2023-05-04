import os, os.path, shutil, re

path = "C:\\My Web Sites\\b1\\s.kaskus.id\\images\\hotbeninginsidepart4"
parent_list = os.listdir(path)
for count3 in range(10):
    for count2 in range(10):
        for count in range(10):
            new_path = "C:\\My Web Sites\\hotbeninginsidepart4\\" + str(count3) + str(count2) + str(count) + "\\"
            images = [f for f in (os.listdir(path)[:50]) if '.jpg']
            if len(images) > 0:
                if not os.path.exists(new_path):
                    os.makedirs(new_path)

                for image in images:
                    new_file_path = new_path + image
                    filename = path + "\\" + image
                    shutil.move(filename, new_file_path)
