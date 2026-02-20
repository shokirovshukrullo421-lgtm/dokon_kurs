import csv
FILE="config/products.csv"
from functions.admin_functions import *
def mahsulot_qoshish():
    with open(FILE, "r", newline="") as f:
        oqi=csv.DictReader(f)
        mahsulotlar=[]
        all_products=[]
        count=0
        for i in oqi:
            all_products.append(i)
            count+=1
            print(f"{count}.  {i["name"]}  {i['price']}  {i["miqdor"]}")
        print()
        choise=input("xarid qilmoqchi bolgan mahsulot nomini kiriting:\n")
        for i in all_products:
            ulgurji=[]
            if i["name"]==choise:
                kg=input("miqdorini kiriting:\n")
                if int( kg) <int(i["miqdor"]):
                    ulgurji.append(i["name"])
                    ulgurji.append(i["price"])
                    ulgurji.append(kg)
                    
                    mahsulotlar.append(ulgurji)
                    print("savatga mahsulot qoshildi")
                else:
                    print("mahsulot yetarli emas")
            else:
                print("bunday mahsulot mavjud emas")
                     