import csv
from functions.qoshimcha import *
USER_DATA = "config/user_data.csv"
def registratsiy():
    print("registratsiya oynasi ochildi")
    try:
        ism = input("Ismingizni kiriting: ")
        login = input("Login kiriting: ")
        parol = input("Parol kiriting: ")
    except:
        print("Kiritishda xatolik")
        return

    with open(USER_DATA, "a", newline="") as f:
        yoz = csv.DictWriter(f,fieldnames=["ism", "login", "parol"])
        if f.tell() == 0:
            yoz.writeheader()
        yoz.writerow({
            "ism": ism,
            "login": login,
            "parol": parol
        })
    print("✅ Saqlandi")
