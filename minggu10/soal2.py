nama = input("nama file1: ")
file = open(nama, "r")
for baris in file:
    bagian = baris.strip().split("||")
    soal = bagian[0].strip()
    jawaban_benar = bagian[1].strip().lower()
    print(soal)
    jawaban_kite = input("Jawab: ").strip().lower()
    if jawaban_kite == jawaban_benar:
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")
file.close()