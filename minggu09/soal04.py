def pakat(kalimat):
    kata = kalimat.replace(",",'').replace('.','').split()

    if not kata:
        return None, None
    
    katapendek = katapanjang = kata[0]
    for c in kata:
        if len(c) < len(katapendek):
            katapendek = c
        if len(c) > len(katapanjang):
            katapanjang = c
    return f"Kata terpendek: {katapendek}, kata terpanjang: {katapanjang}"
print(pakat('aku suka sekali dengan ayam goreng'))
print(pakat('apakah kamu menyukai informatika di ukdw?'))