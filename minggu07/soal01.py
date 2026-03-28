n = int(input("Masukkan nilai n = "))
def prima(angka):
    if angka <= 1:
        return False
    for i in range(2,int(angka**0.5)+1):
        if angka % i == 0:
            return False
    return True

for i in range(n-1, 1, -1):
    if prima(i):
        print("Bilangan prima terdekat < n adalah:",i)
        break

