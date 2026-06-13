def x(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False  
            
    return True  

print(x([1, 2, 3, 4, 5]))  
print(x([5, 3, 2, 1]))     
