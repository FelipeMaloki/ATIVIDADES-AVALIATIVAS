def palindromo(texto):
    limpo = ""
    for letra in texto:
        if letra != " ":
            limpo += letra.lower()
            
    invertido = limpo[::-1]
    
    return limpo == invertido

entrada_usuario = input("Digite uma palavra ou frase para verificar: ")

if palindromo(entrada_usuario):
    print("Saída: True (É um palíndromo!)")
else:
    print("Saída: False (Não é um palíndromo!)")
