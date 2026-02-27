try: 
    a = int(input("Masukkan sisi 1: "))
    b = int(input("Masukkan sisi 2: "))
    c = int(input("Masukkan sisi 3: "))

    if a == b == c:
        print("3 sisi sama")
    elif a == b or a == c or b == c:
        print("2 sisi sama")
    else:
        print("tidak ada yang sama")
except:
    print("input yang dimasukkan salah!")