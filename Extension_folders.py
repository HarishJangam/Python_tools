import os
import shutil

path=input("enter your path")
folder=os.listdir(path)
for i in folder:
    filename,extention=os.path.splitext(i)
    extention_1=extention[1:]
    folder_path=path+"\\"+extention_1
    if os.path.exists(folder_path):
        shutil.move(path+"\\"+i,path+"\\"+extention_1+"\\"+i)
    else:
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i,path+"\\"+extention_1+"\\"+i)