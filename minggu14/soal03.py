try:
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")

    handle1 = open(file1, "r")
    handle2 = open(file2, "r")

    kata1 = set()
    kata2 = set()

    for baris in handle1:
        baris = baris.lower()
        kata = baris.split()

        for k in kata:
            kata1.add(k)

    for baris in handle2:
        baris = baris.lower()
        kata = baris.split()

        for k in kata:
            kata2.add(k)

    sama = kata1.intersection(kata2)

    print("\nKata yang muncul pada kedua file:")
    for k in sorted(sama):
        print(k)

    handle1.close()
    handle2.close()

except FileNotFoundError:
    print("File tidak ditemukan")