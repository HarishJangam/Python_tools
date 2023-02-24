import os
# file=open("hari.txt","w+")


    # for root,dirs,file in os.walk(path):
    #     for f in file:
    #         print(os.path.join(root,f))
# def false(path):
    
#     #method one
#     try:
#         os.mkdir(path)
#     except FileExistsError:
#         print("folder already exist")
    
    
#path=os.getcwd()
# print(path)
# os.mkdir("./hari")
file_name=input("VISITING_REPORT_BAJAJ SHOOWROOM")
print("@@@@@@@@@ Choose folder @@@@@@@@@@@ :")
path="D:"
for root,dir,file in os.walk(path):
    
    for f in file:
        if file_name in f:
            print(os.path.join(root,f))
# print("@@@@@ choose File @@@@@@ :")
# for root,dirs,file in os.walk(path):
    
#     for f in file:
#         # print(dirs)
#         print(f)
            
    # method 2 :
# def create():
# try:
#     path=os.getcwd()
#     os.makedirs(path)
# except FileExistsError:
#     print("folder already exist")

# def template(path):
#     print("hi")
#     print("########   WELCOME TO SMART FILE MANAGER ##########")
#     print("Please select your option :")
#     print("press 2.create a folder")
#     print("press 3.delete a folder")
#     print("press 4.rename a folder")
#     print("press 5.search")
    
    
#     while True :
#         key=int(input())
#         # if key==2:
#         #      create(path)
#         print("enter 1 to exit")
        
#         if key == 1 :
#             break
       
        
# if __name__=="__main__":
#     print("@@@@@@  WELCOME  @@@@@@@")
    
#     path=os.getcwd()
#     template(path)
#     false(path)
    