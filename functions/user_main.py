from functions.admin_functions import *
from config.menus import *
from functions.users_functions import *
def user_panel():
    while True :
        print(user_menu)
        choice=input("tanlang")
        if choice=="1":
            mahsulot_qoshish()
        elif choice=="2":
            while True:
                mahsulot_qoshish()
                print("yana qoshasizmi: ha/yoq")
                tanlash=input("tanlang:\n")
                if tanlash=="ha":
                    return
                elif tanlash=="yoq":
                    break
                else:
                    print("cato tanlov")
        elif choice=="3":
            pass
        elif choice=="4":
            pass
        elif choice=="5":
            pass
            break
        else:
            print("xato tanlov")