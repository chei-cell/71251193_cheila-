nama = input("Masukkan nama file : ")

handle = open(nama, "r")

email_count = {}

for baris in handle:
    if baris.startswith("From "):
        kata = baris.split()
        email = kata[1]

        email_count[email] = email_count.get(email, 0) + 1

print(email_count)