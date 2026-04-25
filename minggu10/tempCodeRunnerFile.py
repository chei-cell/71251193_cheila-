handle1 = open((input("Nama file 1 : ")), "r")
handle2 = open((input("Nama file 2 : ")), "r")

baris1 = handle1.readlines()
baris2 = handle2.readlines()
berbeda = False

maks_baris = max(len(baris1), len(baris2))

for i in range(maks_baris):
    teks1 = baris1[i].strip() if i < len(baris1) else ""
    teks2 = baris2[i].strip() if i < len(baris2) else ""

    if teks1 != teks2:
        berbeda = True
        print(f"Perbedaan pada baris {i+1}:")
        print(f"File 1: {teks1}")
        print(f"File 2: {teks2}")
        print()
if berbeda == False : 
    print("Kedua file isinya sama")

handle1.close()
handle2.close()