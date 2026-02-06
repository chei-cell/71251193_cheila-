uang_erika = 200000000
minimal_saldo = 400000000
bunga = 10/100 
tahun_nabung = 0 

while uang_erika < minimal_saldo :
    uang_erika += uang_erika * bunga
    tahun_nabung += 1 
print(f"waktu yang dibutuhkan : {tahun_nabung:}tahun")

