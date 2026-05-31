def cek_prima(n, pembagi=2):  
    if n < 2: 
        return False 
    if pembagi > n ** 0.5: 
        return True 
    if n % pembagi == 0: 
        return False 
    return cek_prima(n, pembagi + 1) 
print(cek_prima(5)) 
print(cek_prima(19)) 
print(cek_prima(28)) 
