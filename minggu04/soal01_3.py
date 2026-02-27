try:
    a = int(input("masukkan nilai a: "))
    b = int(input("masukkan nilai b: "))
    c = int(input("masukkan nilai c: "))
    
    if a > b and a > c :
        print("Terbesar: ", a)
    elif b > a and b > c :
        print("Terbesar: ", b)
    elif c > a and c > b :
        print("Terbesar: ",c) 
except:
    print("input nya salah!")