import os
folder_path="/Users\janga\OneDrive\Desktop\development_tools"
def directory_files(dir) :
    file_names=os.listdir(dir)
    for file in file_names:
        print("fileName : "+file) 
if __name__=='__main__':
    directory_files(folder_path)