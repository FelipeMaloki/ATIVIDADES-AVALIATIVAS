def contar_caracteres(texto):
    frequencia = {}
    
    for caractere in texto:
        
        if caractere in frequencia:
            frequencia[caractere] += 1
        
        else:
            frequencia[caractere] = 1
            
    return frequencia

print(contar_caracteres("abacaxi"))

