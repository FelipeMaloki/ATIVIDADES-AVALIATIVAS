def contar_vogais(texto):
    vogais = "aeiouáéíóúâêîôûãõàèìòù"
    contador = 0
    
    for letra in texto.lower():
        if letra in vogais:
            contador += 1
            
    return contador
print(contar_vogais("Programação"))  

