def multiplicacao(a, b):
    resultado = 0
    
    while b > 0:
        resultado += a
        b -= 1 
    while b < 0:
        resultado -= a
        b += 1 
        
    return resultado

print(multiplicacao(6, 7))    
print(multiplicacao(-6, 7))   
print(multiplicacao(6, -7))   
print(multiplicacao(-6, -7))  

