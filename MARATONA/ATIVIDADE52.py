def anagrama(str1, str2):

    limpa1 = ""
    for letra in str1:
        if letra != " ":
            limpa1 += letra.lower()
    limpa2 = ""
    for letra in str2:
        if letra != " ":
            limpa2 += letra.lower()

    if len(limpa1) != len(limpa2):
        return False
    
    contagem1 = {}
    for letra in limpa1:
        if letra in contagem1:
            contagem1[letra] += 1
        else:
            contagem1[letra] = 1

    contagem2 = {}
    for letra in limpa2:
        if letra in contagem2:
            contagem2[letra] += 1
        else:
            contagem2[letra] = 1

    return contagem1 == contagem2


print(anagrama("amor", "roma"))    
print(anagrama("python", "java"))  
