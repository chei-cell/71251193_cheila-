file = input("Enter a file name: ")
handle = open(file)

jam_count = {}

for baris in handle:
    if baris.startswith("From "):
        kata = baris.split()
        
        waktu = kata[5]
        
        jam = waktu.split(":")[0]
        
        jam_count[jam] = jam_count.get(jam, 0) + 1

for jam, jumlah in sorted(jam_count.items()):
    print(jam, jumlah)