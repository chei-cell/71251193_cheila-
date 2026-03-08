def cek_angka(x,y,z):
    if x == y or x == z or y == z:
        return False
    if x+y == z or x+z == y or y+z == x:
        return True
    else: 
        return False 
    
#testcase
print(cek_angka(30,50,60))
print(cek_angka(5,2,10))
print(cek_angka(20,40,60))
print(cek_angka(5,2,7))