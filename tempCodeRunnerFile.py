import os
import shutil

def LIst_of_All_folders(directory):
        #print(os.getcwd())
        #directory=os.getcwd()
        folders = []
        for root, dirs, files in os.walk(directory):
                for file in dirs:
                        folders.append(os.path.join(root,file))
        
        for f in folders:
                print(f)
def change_folder():
        print("enter folder name which u want to go : ")
        LIst_of_All_folders()
        folder=input("folder_name : ")
        print("folder path :",os.getcwd())
        os.chdir(folder)
def crete():
        folder=input("enter folder name : ")
        path=os.getcwd()
        print(path)
        try:
                os.makedirs(path+"\\"+folder)
                print("folder created successfully.")
        except:
                print("folder already exist.")
        
def delete():
        print("enter folder name which folder you want to delete")
        folder=input("folder name: ")
        try:
                path=os.getcwd()
                os.rmdir(path+folder)
                print("deleted")
        except:
                print("folder not exist")
                
                
                
def rename_folder(path, name):
    try:
        os.rename(path, os.path.join(os.path.dirname(path), name))
        print(f"Folder '{path}' renamed to '{name}' successfully")
    except OSError as e:
        print(f"Error renaming folder: {e}")


def template(n,directory):
      if(n==1):
               LIst_of_All_folders(directory)
      elif(n==2):
              crete()
      elif(n==3):
              delete()
      elif(n==4):
              change_folder()
              

if __name__=="__main__":
        # print("enter path")
        directory=input("enter D or C :")
        # try:
        #         path=input("enter path:")
        #         os.chdir(path)
        # except:
        #         print("folder not exist")
        t=0
        LIst_of_All_folders(directory)
        print("enter path from and name ")
        path=input("path :")
        name=input("name :")
        rename_folder(path,name)
        while(t):
                print("""enter 1.To See All folders
                2.Create New folder
                3.Delete folder
                4.change dir """)
                choice=int(input("enter option : "))
                template(choice,directory)
                t=t-1
