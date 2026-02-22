from functions.admin_functions import *
from config.menus import *
def admin_panel():
    while True :
        print(admin_menu)
        choice=input("tanlang")
        if choice=="1":
            mahsulot_qoshis()
        elif choice=="2":
            barcha_mahsulotla()
        elif choice=="3":
            mahsulot_ochirish()
        elif choice=="4":
            userlarni_korish()
        elif choice=="5":
            xarid_tarixi()
            
        elif choice=="6":
            print("Admin panelidan chiqildi")
            break
        else:
            print("xato tanlov")