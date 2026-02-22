import csv
import ast

FILE = "config/products.csv"
DATA = "config/data.csv"

def mahsulotlarni_korish():
    with open(FILE, "r", newline="", encoding="utf-8") as file:
        data = list(csv.DictReader(file))

    print("\n📦 Mavjud mahsulotlar:")
    for i in data:
        print(f"{i['name']} | Narxi: {i['price']} | Qolgan: {i['miqdor']}")
def savatga_qoshish(cart):
    while True:
        with open(FILE, "r", newline="", encoding="utf-8") as file:
            products = list(csv.DictReader(file))

        if not products:
            print("❌ Omborda mahsulot yo‘q")
            return

        print("\n📦 Mavjud mahsulotlar:")
        for p in products:
            print(f"{p['name']} | Narxi: {p['price']} | Qolgan: {p['miqdor']}")
        name = input("\nMahsulot nomini kiriting (yoki '0' chiqish): ")
        if name == "0":
            return
        for product in products:
            if product['name'] == name:
                mavjud = int(product['miqdor'])
                narx = int(product['price'])
                break
        else:
            print("❌ Mahsulot topilmadi")
            continue
        try:
            miqdor = int(input("Miqdor: "))
        except ValueError:
            print("❌ Noto‘g‘ri son")
            continue

        if miqdor <= 0:
            print("❌ Miqdor 0 dan katta bo‘lishi kerak")
            continue
        if miqdor > mavjud:
            print("❌ Omborda yetarli mahsulot yo‘q")
            continue
        for item in cart:
            if item[0] == name:
                item[1] += miqdor
                item[2] += narx * miqdor
                break
        else:
            cart.append([name, miqdor, narx * miqdor])

        print("✅ Savatga qo‘shildi")
        yana = input("\nYana mahsulot qo‘shasizmi? (ha/yoq): ").lower()
        if yana != "ha":
            break
def savatni_korish(login, cart):
    if not cart:
        print("🛒 Savat bo‘sh")
        return
    print("\n🛒 Savatingiz:")
    total = 0
    for i in cart:
        print(f"{i[0]} | {i[1]} ta | {i[2]} so'm")
        total += i[2]

    print(f"💰 Umumiy: {total}")
    tasdiq = input("To‘lovni tasdiqlaysizmi? (ha/yoq): ")
    if tasdiq == "ha":
        savatni_saqlash(login, cart, total)
        cart.clear()
        print("✅ Xarid amalga oshirildi")
    else:
        print("↩️ User menu ga qaytdingiz")
def savatni_saqlash(login, cart, total):
    try:
        with open(DATA, "r", newline="", encoding="utf-8") as file:
            data = list(csv.DictReader(file))
    except FileNotFoundError:
        data = []
    if data and "login" not in data[0]:
        data = []
    topildi = False
    for row in data:
        if row.get("login") == login:
            eski = ast.literal_eval(row["royxat"])
            eski.extend(cart)
            row["royxat"] = str(eski)
            row["total_price"] = str(int(row["total_price"]) + total)
            topildi = True
            break
    if not topildi:
        data.append({
            "login": login,
            "royxat": str(cart),
            "total_price": str(total)
        })
    with open(DATA, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["login", "royxat", "total_price"])
        writer.writeheader()
        writer.writerows(data)
def savatni_tahrirlash(cart):
    if not cart:
        print("🛒 Savat bo‘sh")
        return
    print("1. O‘chirish")
    print("2. Miqdor o‘zgartirish")
    tanlov = input("Tanlang: ")
    name = input("Mahsulot nomi: ")
    for item in cart:
        if item[0] == name:
            if tanlov == "1":
                cart.remove(item)
                print("✅ O‘chirildi")
                return
            elif tanlov == "2":
                try:
                    yangi = int(input("Yangi miqdor: "))
                except:
                    print("❌ Noto‘g‘ri son")
                    return
                if yangi <= 0:
                    print("❌ Noto‘g‘ri miqdor")
                    return
                narx_bir_dona = item[2] // item[1]
                item[1] = yangi
                item[2] = narx_bir_dona * yangi
                print("✅ Yangilandi")
                return
    print("❌ Mahsulot topilmadi")