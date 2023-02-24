import os
import shutil


# function to get the list of all folders and subfolders
def get_folders(directory):
    
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            print(os.path.join(root, name))
    

# function to create a folder
def create_folder(path, name):
    try:
        os.mkdir(os.path.join(path, name))
        print(f"Folder '{name}' created successfully in '{path}'")
    except OSError as e:
        print(f"Error creating folder: {e}")

# function to delete a folder
def delete_folder(path):
    try:
        shutil.rmtree(path) 
        print(f"Folder '{path}' deleted successfully")
    except OSError as e:
        print(f"Error deleting folder: {e}")

# function to rename a folder
def rename_folder(path, name):
    try:
        os.rename(path, os.path.join(os.path.dirname(path), name))
        print(f"Folder '{path}' renamed to '{name}' successfully")
    except OSError as e:
        print(f"Error renaming folder: {e}")

# function to open a folder
def open_folder(path):
    try:
        os.startfile(path)
    except OSError as e:
        print(f"Error opening folder: {e}")

# function to search for files
def search_files(directory, query, exact_match=False, pattern_match=False, extension_match=None):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            if exact_match:
                if query == name:
                    results.append(os.path.join(root, name))
            elif pattern_match:
                if query in name:
                    results.append(os.path.join(root, name))
            elif extension_match:
                if name.endswith(extension_match):
                    results.append(os.path.join(root, name))
    for f in results:
        print(f)

# function to manage storage
def manage_storage(path, max_folder_size, max_file_size):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            if total_size > max_folder_size:
                print(f"Error: Maximum folder size reached: {max_folder_size} bytes")
                return False
            elif os.path.getsize(fp) > max_file_size:
                print(f"Error: Maximum file size reached: {max_file_size} bytes")
                return False
    return True

# function to sort files by name, size or extension
def sort_files(directory, sort_by):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    if sort_by == 'name':
        files.sort()
    elif sort_by == 'size':
        files.sort(key=os.path.getsize)
    elif sort_by == 'ext':
        files.sort(key=lambda s: os.path.splitext(s)[1])

    return files
def template():
    print("""enter ur option :
        1.get_folders():
        2.open_folder():
        3.search_files()
          """)
    option=int(input())
    if(option==1):
        
        get_folders()
    elif(option==2):
        open_folder()
    elif(option==3):
        search_files()
if __name__=="__main__":
     directory=input("enter directory : ")
     get_folders(directory)
     
    #  path=input("enter path :")
    #  open_folder(path)
    #  delete_folder(path)
    # # print("open folder path")
    # # path=input("path :")
    # # open_folder(path)
    # print("search a file : ")
     search_files("D:",None,False,False,".pdf")
    # template()