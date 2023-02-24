from pdf2docx import Converter
from docx2pdf import convert
# try:
#     old_pdf=input("enter pdf name which u want to convert with .pdf extension: ")
#     new_docx=input("enter name which name u want for ur docx name with .docx :")
#     obj=Converter(old_pdf)
#     obj.convert(new_docx)
# except:
#     print("check once ur given names ")
  
try:  
    old_docx=input("enter name .docx of u want : ")
    new_pdf=input("enter name of pdf to convert : ")
    convert(old_docx,new_pdf)
except:
    print("check entered names and formates once....")