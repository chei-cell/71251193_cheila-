#masukkan input yang diperintahkan soal
tinggibadan = float(input("Masukkan tinggi badan anda (m) = "))
nilaibody = float(input("Masukkan nilai body mass index anda = "))

#langkah-langkah untuk menghitung berat badan 
beratbadan = round(nilaibody * (tinggibadan**2),2)

print(f"Masukkan berat badan anda = {beratbadan} ")