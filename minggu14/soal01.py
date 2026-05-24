jml_kategori = int(input("Masukkan jumlah kategori: "))

kategori = {}

for i in range(jml_kategori):
    nama = input(f"\nMasukkan nama kategori ke-{i+1}: ")

    jmlh_aplikasi = int(input("Masukkan jumlah aplikasi/game: "))

    data_aplikasi = set()

    for j in range(jmlh_aplikasi):
        aplikasi = input(f"Masukkan aplikasi ke-{j+1}: ")
        data_aplikasi.add(aplikasi)

    kategori[nama] = data_aplikasi

hitung = {}

for nama in kategori:
    for aplikasi in kategori[nama]:
        hitung[aplikasi] = hitung.get(aplikasi, 0) + 1

print("\nAplikasi yang hanya muncul di satu kategori:")
for aplikasi, jumlah in hitung.items():
    if jumlah == 1:
        print("-", aplikasi)

print("\nAplikasi yang muncul tepat di dua kategori:")
for aplikasi, jumlah in hitung.items():
    if jumlah == 2:
        print("-", aplikasi)