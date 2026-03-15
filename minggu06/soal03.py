def hitung():
    jumlah_Mk = int(input("Berapa jumlah mata kuliah? "))
    nilai = 0 
    sks = 3
     
    for i in range(1, jumlah_Mk +1):
        predikat = input(f"Nilai MK{i}:")

        if predikat == "A":
            bobot = 4
        elif predikat == "B":
            bobot = 3
        elif predikat == "C":
            bobot = 2
        elif predikat == "D":
            bobot = 1
        
        nilai = nilai + (bobot * sks)
    total = jumlah_Mk * sks
    ips = nilai/total

    print(f"IPS Anda = {ips: .2f}")
hitung()