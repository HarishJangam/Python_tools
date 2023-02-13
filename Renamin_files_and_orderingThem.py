import os
os.chdir('/Users\janga\OneDrive\Desktop\FullStack/bootsrap')
print(os.getcwd())
#print(os.listdir())
for f in os.listdir():
	file_name,file_ext=os.path.splitext(f)
	num,name=file_name.split('-')
	file_ext=file_ext.strip()
	num=num.strip()
	name=name.strip()
	#print('{}.{}{}'.format(num,name,file_ext))
	newname='{}.{}.{}'.format(num,name,file_ext)
	os.rename(f,newname)
	#print(f)

