try:
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan > 0 :
        print("bilangan positif")
    elif bilangan < 0 :
        print("bilangan negatif")
    elif bilangan == 0:
        print("nol")
except: 
    print("maaf input anda salah!")