def string(lista):
    maior = lista[0]
    
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
            
    return maior

print(string(["casa", "carro", "avião"]))  