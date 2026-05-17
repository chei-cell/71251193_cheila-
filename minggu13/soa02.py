nama = input("Masukkan nama : ")
nim = input("Masukkan NIM : ")
alamat = input("Masukkan alamat : ")
data = (nama, nim, alamat)

print("\nDATA")
print("NIM   :", data[1])
print("NAMA  :", data[0])
print("ALAMAT:", data[2])

nim = tuple(data[1])
print("\nNIM:", nim)

nama_depan = tuple(data[0].split()[0])
print("\nNAMA DEPAN:", nama_depan)

nama_balik = tuple(reversed(data[0].split()))
print("\nNAMA TERBALIK:", nama_balik)