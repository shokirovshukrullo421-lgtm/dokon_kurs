from functions.users_functions import *
from config.menus import *
def user_panel(login):
    cart = []

    while True:
        print(user_menu)
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            mahsulotlarni_korish()

        elif tanlov == "2":
            savatga_qoshish(cart)

        elif tanlov == "3":
            savatni_korish(login, cart)

        elif tanlov == "4":
            savatni_tahrirlash(cart)

        elif tanlov == "5":
            print("👋 Chiqdingiz")
            break

        else:
            print("❌ Noto‘g‘ri tanlov")