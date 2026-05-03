handle = open("file.txt", "r")

coba = set()

for baris in handle:
    kata = baris.split()
    for k in kata:
        coba.add(k)

print(coba)