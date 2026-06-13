def remover(texto):
    resultado = ""
    
    for letra in texto:
        if letra not in resultado:
            resultado += letra
            
    return resultado

print(remover("banana")) 
