def maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort()
    return lista_unica[-2]

print(maior([10, 20, 4, 45, 99, 99]))  
