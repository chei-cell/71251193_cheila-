def palindrome(kata):
    kata = kata.lower().replace(" ", "")
    if len(kata) <= 1:
        return True

    if kata[0] != kata[-1]:
        return False

    return palindrome(kata[1:-1])

print(palindrome("monyet"))
print(palindrome("radar"))
print(palindrome("java"))