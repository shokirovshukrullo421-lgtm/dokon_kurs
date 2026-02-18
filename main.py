from config.config_init import *
from register.registratsiya import *    
from config.menus import *
from register.login import *
init_users_file()
init_products_file()
while True:
    print(auth_menu)
    try:
        tanlov = int(input("Tanlovni kiriting: "))
    except:
        print("Kiritishda xatolik")
        continue
    if tanlov == 1:
        registratsiy()
    elif tanlov == 2:
        login()
    elif tanlov == 3:
        print("Dasturdan chiqildi")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")
