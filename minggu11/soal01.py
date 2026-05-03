def bilanganbaik(list):
    list.sort(reverse=True) 
    return list[:3]   
       
data = [10, 5, 8, 20, 3, 15]
print(bilanganbaik(data))
print(bilanganbaik([100,23,145,67,89,23,123,456,789]))