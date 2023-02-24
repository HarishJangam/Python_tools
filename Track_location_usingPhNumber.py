import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

num=input("enter ph number")
ch_num=phonenumbers.parse(num,"CH")
print(geocoder.description_for_number(ch_num,"en"))
service_name=phonenumbers.parse(num,"RO")
print(carrier.name_for_number(service_name,"en"))