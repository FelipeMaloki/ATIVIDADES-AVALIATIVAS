def calcular_media(nota1, nota2):
    
    return (nota1 + nota2) / 2

def exercicio_funcoes():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    
    media_final = calcular_media(n1, n2)
    print(f"A média retornada pela função é: {media_final}")