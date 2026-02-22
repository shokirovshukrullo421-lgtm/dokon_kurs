import csv

viloyatlar = {}

with open("72A-TTJ.csv", newline='', encoding="cp1251") as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # headerni tashlab ketamiz

    for row in reader:
        if len(row) > 4 and row[4].strip() != "":
            manzil = row[4]

            # Viloyatni aniqlash
            if "Viloyati" in manzil:
                viloyat = manzil.split("Viloyati")[0].strip()
            elif "Respublikasi" in manzil:
                viloyat = manzil.split("Respublikasi")[0].strip()
            elif "shahar" in manzil.lower():
                viloyat = "Toshkent shahar"
            else:
                viloyat = "Noma'lum"

            # Hisoblash
            if viloyat in viloyatlar:
                viloyatlar[viloyat] += 1
            else:
                viloyatlar[viloyat] = 1

# Natija chiqarish
yigindi=0
count=0
for v, soni in viloyatlar.items():
    yigindi+=soni
    count+=1
    print(f"{count}. {v}: {soni} ta")   
print("Jami:", yigindi)