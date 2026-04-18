import re

kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata: ")

def jumlah(kalimat, kata):
    kalimat = kalimat.lower()
    kata = kata.lower()
    daftar_kata = re.findall(r"[a-z0-9']+", kalimat)
    jumlah = daftar_kata.count(kata)
    
    return jumlah

hasil = jumlah(kalimat, kata)
print(f"Kata '{kata}' ada {hasil} buah")