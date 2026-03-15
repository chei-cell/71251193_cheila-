bawah = int(input("Masukkan Bilangan Bawah : "))
atas = int(input("Masukkan Bilangan Atas : "))

def ganjil (atas, bawah):
    if bawah < atas :
        for i in range(bawah, atas + 1):
            if i%2 !=0:
                print(i,end=" ")
    else:
        for i in range(bawah, atas -1,-1 ):
            if i%2 !=0:
                print(i,end=" ")
ganjil(atas,bawah)