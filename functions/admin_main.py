from functions.admin_functions import *
from config.menus import *
def admin_panel():
    while True :
        print(admin_menu)
        choice=input("tanlang")
        if choice=="1":
            mahsulot_qoshish()
        elif choice=="2":
            pass
        elif choice=="3":
            pass
        elif choice=="4":
            pass
        elif choice=="5":
            pass
        elif choice=="6":
            print("Admin panelidan chiqildi")
            break
        else:
            print("xato tanlov")