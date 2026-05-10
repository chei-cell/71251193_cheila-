satu = input("Masukkan warna (pisahkan dengan spasi): ").split() 
dua = input("Masukkan kode warna (pisahkan dengan spasi): ").split()
hasil = dict(zip(satu, dua)) 
print(hasil)