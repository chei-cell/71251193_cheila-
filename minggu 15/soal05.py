def cari_kombinasi(n, k): 
    if k == 0 or k == n: 
        return 1 
    return cari_kombinasi(n-1, k-1) + cari_kombinasi(n-1, k) 
print(cari_kombinasi(5, 2))  
print(cari_kombinasi(4, 2))   
print(cari_kombinasi(7, 3)) 