def cek_digit_belakang(x,y,z):
    digit_x = x%10
    digit_y = y%10
    digit_z = z%10

    if digit_x == digit_y or digit_x == digit_z or digit_y == digit_z:
        return True
    else:
        return False

#ini testcase nya 
print(cek_digit_belakang(30,20,18))
print(cek_digit_belakang(145,5,100)) 
print(cek_digit_belakang(71,187,18)) 
print(cek_digit_belakang(1024,14,94)) 
print(cek_digit_belakang(53,8900,658))  