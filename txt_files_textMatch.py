import os
import pandas as pd
import numpy as np
souce_folder="/Users\janga\OneDrive\Desktop\C++\CppFiles/"
desti_folder="/Users\janga\OneDrive\Desktop\C++\cpp"
diclist=os.listdir(souce_folder)
ss="11"
file_list=[]
for file in diclist:
    if file.endswith('.txt'):
        f=open(souce_folder+file,"r")
        if ss in f.read():
            file_list.append(file)
        f.close()
        
print(file_list)
stringFile=pd.DataFrame(file_list,columns=['FileName'],index=range(0,len(file_list)))
print(stringFile)
# stringFile.to_excel(desti_folder+"stringFile.xlsx",index=False)
# print(stringFile)