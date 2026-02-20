from decouple import config
import csv
from config.menus import *
from functions.admin_main import *
from functions.admin_functions import *
from functions.user_main import *
USER_FILE="config/user_data.csv"
USER_DATA = config("USER_FILE")

ADMIN_LOGIN = config("ADMIN_LOGIN")
ADMIN_PASSWORD = config("ADMIN_PAROL")


def login():
    print("Login oynasi")

    login = input("Login: ")
    parol = input("Parol: ")
    if login == ADMIN_LOGIN and parol == ADMIN_PASSWORD:
        print("✅ Admin sifatida kirdingiz")
        admin_panel()
        
        
        
    
        return

    # ✅ 2 — ODDIY USER TEKSHIRISH
    with open(USER_DATA, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["login"] == login and row["parol"] == parol:
                print(f"✅ Xush kelibsiz {row['ism']}")
                user_panel()
                return

    print("❌ Login yoki parol xato")
