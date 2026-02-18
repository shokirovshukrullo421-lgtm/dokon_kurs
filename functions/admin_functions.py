import csv
from decouple import config
FILE="config/products.csv"
def mahsulot_qoshish():
    with open( FILE, "a", newline="") as f:
        while True:
            product_name=input("mahsulotni nomini kiriting:\n")
            product_price=input("mahsulotni narxini kiriting:\n")
            product_miqdor=input("mahsulotni miqdorini kiriting:\n")
            yoz = csv.DictWriter(f,fieldnames=["name", "price", "miqdor"])
            if f.tell() == 0:
                yoz.writeheader()
            yoz.writerow({
                "name": product_name,
                "price": product_price,
                "miqdor": product_miqdor
                })
            print("✅ Saqlandi")
            print("yana mahsulot kiritasizmi: ha / yoq")
            choice=input("tanlang:\n")
            if choice=="ha":
                continue
            elif choice=="yoq":
                print("mahsulot kiritish tugadi")
                break
            else:
                print('xato tanlov')
        