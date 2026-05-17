jmlh = int(input("Masukkan jumlah anggota list: "))
data = []
for c in range(jmlh):
    angka = int(input(f"Masukkan angka ke-{c+1}: "))
    data.append(angka)
c = all(x == data[0] for x in data)

print(c)