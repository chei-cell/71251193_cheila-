def perkalian(x, y):
    hasil = 0
    for i in range(x):
        hasil = hasil + y
        print(y, end="")
        if i < x-1:
            print(" + ", end="")
    print(" =", hasil)

def jalan(x,y):
    print(x, "x", y, " =", end=" ")
    perkalian(x, y)

#testcase sesuai soal
jalan(5, 6)
jalan(7, 10)
jalan(8,8)