n = int(input("Masukkan nilai n = "))
for i in range(n,0,-1):
    fakotrial = 1
    for c in range(1,i+1):
        fakotrial *= c
    print(fakotrial, end=" ")
    for j in range(i, 0 ,-1):
        print(j, end=" ")
    print()