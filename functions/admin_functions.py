import csv
from decouple import config
import ast
DATA = "config/data.csv"
FILE="config/products.csv"
USER_FILE="config/user_data.csv"
def mahsulot_qoshis():
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
def barcha_mahsulotla():
    with open(FILE, "r", newline=""  ) as f:
        oqi=csv.DictReader(f)
        for i in oqi:
            print(f"nomi->({i["name"]})  narxi->({i["price"]})  miqdori->({i["miqdor"]})")       
 
def mahsulot_ochirish():
    massiv=[]
    name=input("ochirmoqchi bolgan mahsulot name:\n")
    with open(FILE, 'r', newline="") as f:
        oqi=csv.DictReader(f)
        for i in oqi:
            if i["name"]==name:
                pass
            else:
                massiv.append(i)
    with open(FILE, "w", newline='') as f:
        yoz = csv.DictWriter(f,fieldnames=["name", "price", "miqdor"])
        if f.tell() == 0:
            yoz.writeheader()
        for i in massiv:
            yoz.writerow({
                "name":i["name"],
                "price":i["price"],
                "miqdor":i["miqdor"]
            })
    print("yangilandi")
def userlarni_korish():
    count=0
    with open(USER_FILE, "r", newline="") as f:
        print("barcha userlar")
        oqi=csv.DictReader(f)
        for i in oqi:
            count+=1
            print(f"{count}. {i["ism"]}  {i["login"]}  {i["parol"]}")
def xarid_tarixi():
    try:
        with open(DATA, "r", newline="", encoding="utf-8") as file:
            data = list(csv.DictReader(file))
    except FileNotFoundError:
        print("❌ Xarid tarixi mavjud emas")
        return

    if not data:
        print("❌ Hali hech kim xarid qilmagan")
        return

    print("\n" + "="*50)
    print("🛒 XARID TARIXI")
    print("="*50)

    for row in data:
        print(f"\n👤 Login: {row['login']}")
        print("-"*40)

        try:
            royxat = ast.literal_eval(row["royxat"])
        except:
            print("❌ Royxat o‘qilmadi")
            continue

        for item in royxat:
            # item = [name, quantity, price]
            print(f"📦 {item[0]} | {item[1]} ta | {item[2]} so'm")

        print(f"💰 Jami: {row['total_price']} so'm")
        print("-"*40)

    print("="*50)