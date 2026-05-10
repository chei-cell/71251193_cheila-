input = input("Dictionary : ")

dict = eval(input)

print("key\tvalue\titem")

for key, value in dict.items():
    print(key, "\t", value, "\t", key)