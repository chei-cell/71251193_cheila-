try: 
    bilangan = int(input("masukkan bilangan: "))
    nilai_bilangan = "positif" if bilangan > 0 else "negatif" if bilangan < 0 else "nol" 
    print(nilai_bilangan)
except:
    print("input salah!")