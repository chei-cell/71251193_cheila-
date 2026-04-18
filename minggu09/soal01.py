kata1 = input('Masukkan kata pertama: ')
kata2 = input('Masukkan kata kedua: ')

def cekAnagram(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()

    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)

if cekAnagram(kata1, kata2):
    print(f"'{kata1}' dan '{kata2}' adalah anagram")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram")