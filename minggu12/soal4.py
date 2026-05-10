file = input("Masukkan nama file : ")
handle = open(file, "r")
domain_count = {}
for baris in handle:
    if baris.startswith("From "):
        kata = baris.split()
        email = kata[1]

        domain = email.split("@")[1]

        domain_count[domain] = domain_count.get(domain, 0) + 1

print(domain_count)