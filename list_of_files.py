import os
import glob



folder_path=input("enter directry : ")
def directory_files(dir) :
    
    
    ##########  FIRST METHON IT SHOWS ONLY THAT FOLDER FILES   ######
    # file_names=os.listdir(dir)
    # for file in file_names:
    #     print("fileName : ",os.path.join(folder_path,file))
    
    
    ###############################################
    ##  SECOND METHOD IS SHOWS FROM ROOT AND SUB FOLDER FILES ALSO   ###   
    file=input("entr file name: ")
    for root,dirs,file in os.walk(folder_path):
        for f in file :
            name,ext=os.path.splitext(f)
            print(name)
        
    
    ##############################################
    
    ###### THIRD IT SHOW SPECIFIC .EXCENTION FILES ALSO   #####
    # g=glob.glob("*.py")
    # for f in g:
    #     print(os.path.join(folder_path,f))
    
    
if __name__=='__main__':
    directory_files(folder_path)