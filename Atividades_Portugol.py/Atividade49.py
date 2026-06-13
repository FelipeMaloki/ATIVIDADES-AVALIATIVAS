# Definição da função que verifica se o caractere é uma vogal
def verificar_vogal(letra_informada):
    letra_limpa = letra_informada.strip().lower()
    
    if len(letra_limpa) != 1 or not letra_limpa.isalpha():
        return "invalido"
    
    elif letra_limpa in "aeiou":
        return "vogal"
    
    else:
        return "nao_vogal"


print("=== VERIFICADOR DE VOGAIS COM FUNÇÃO ===")

entrada = input("Digite uma letra do alfabeto: ")

resultado = verificar_vogal(entrada)

print("\n-----------------------------------------")
if resultado == "vogal":
    print(f"Resultado: A letra '{entrada}' é uma VOGAL.")
elif resultado == "nao_vogal":
    print(f"Resultado: A letra '{entrada}' é uma NÃO VOGAL (Consoante).")
else:
    print("Resultado: Erro! Você não digitou uma letra válida do alfabeto.")
print("-----------------------------------------")
