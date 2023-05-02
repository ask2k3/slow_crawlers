import os, os.path, shutil


dire = "C:\\Users\\ykhan\\Downloads\\bkup\\gall\\img12\\"

temp = os.walk(dire, topdown=False)
c1=c2=0
for root, dirs, files in temp:
    for i in dirs:
        oldfoldernameandpath = os.path.join(root, i)
        oldfolderpath = os.path.join(root)
        os.rename(oldfoldernameandpath, oldfolderpath + "\\" + str(int(c1/10)) + str(int(c2%10)))
        c1+=1
        c2+=1













