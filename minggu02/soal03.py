#Masukkan input
gajiperjam = float(input("Masukkan gaji per jam: "))
jumlahjamkerja = float(input("Masukkan jumlah jam kerja: "))

#Masukkan langkah-langkah 
#menghitung sblm pajak 
lamakerja = 5
pendapatansblmpajak = round((gajiperjam * jumlahjamkerja * lamakerja),2)
#menghitung setelah pajak 
totalpajak = 14/100
pendapatanstlhpajak = round((pendapatansblmpajak - (pendapatansblmpajak * totalpajak)),2)
#menghitung uang belanja
baju_aksesoris = 10/100
uangbelibajuaksesoris = round((pendapatanstlhpajak * baju_aksesoris),2)
alattulis= 1/100
uangbelialattulis = round((pendapatanstlhpajak * alattulis),2)
pendapatan = pendapatanstlhpajak - (uangbelibajuaksesoris + uangbelialattulis)
#menghitung uang sedekah
sedekah = 25/100 
uangsedekah = round((pendapatan * sedekah),2)
anakyatim = 30/100
uangyatim = round((uangsedekah * anakyatim),2)
kaumdhuafa = round((uangsedekah - uangyatim),2)

print(f"pendapatan budi selama libur sebelum pajak? {pendapatansblmpajak}")
print(f"pendapatan budi selama libur setelah pajak? {pendapatanstlhpajak}")
print(f"Jumlah uang yang digunakan membeli pakaian dan aksesoris? {uangbelibajuaksesoris}")
print(f"Jumlah uang yang dihabiskan membeli alat tulis? {uangbelialattulis}")
print(f"Jumlah uang yang dihabiskan untuk sedekah? {uangsedekah}")
print(f"Jumlah uang untuk anak yatim? {uangyatim}")
print(f"Jumlah uang untuk kaum dhuafa? {kaumdhuafa}")