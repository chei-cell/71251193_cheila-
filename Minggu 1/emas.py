emas1 = 25 
harga_awal_emas = 650000
harga_sekarang = 685000
modal_awal = harga_awal_emas * emas1
modal_awal2 = harga_sekarang * emas1

keuntungan_satu = modal_awal2 - modal_awal
presentase_satu = (keuntungan_satu / modal_awal) * 100

print(f"Keuntungan awal (Rp) : {keuntungan_satu}")
print(f"Keuntungan awal (%) : {presentase_satu:.2f}%")

harga_besok = 715000
emas2 = 40 
total_sekarang = harga_besok * emas2
emas_nambah = emas2 - emas1

keuntungan_dua = (total_sekarang) - (modal_awal) - (harga_sekarang * (emas_nambah))
presentase_dua = (keuntungan_dua / ((modal_awal)+( harga_sekarang * (emas_nambah)))) * 100

print(f"Keuntungan total (Rp) : {keuntungan_dua}")
print(f"Keuntungan total (%) : {presentase_dua:.2f}%")