def jumlah_ganjil(n):
    if n == 1:
        return 1

    return n + jumlah_ganjil(n - 2)
print(jumlah_ganjil(7))