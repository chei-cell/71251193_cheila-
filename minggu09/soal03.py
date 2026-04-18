def menghapus(kalimat):
    kata = kalimat.split()
    kataPojok = ' '.join(kata)
    return kataPojok
print(menghapus('pra alpro  menyenangkan  '))
print(menghapus('  ayo     gas'))