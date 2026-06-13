def inverter_palavras(texto):
    palavras = texto.split()
    resultado = ""
    
    for palavra in palavras:
        palavra_invertida = palavra[::-1]
        if resultado != "":
            resultado += " "
            
            resultado += palavra_invertida
        
    return resultado

print(inverter_palavras("Olá mundo")) 
