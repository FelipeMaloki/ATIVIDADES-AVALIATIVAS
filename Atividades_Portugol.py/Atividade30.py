entrada = input("Digite uma letra: ")

letra = entrada.strip().lower()

if len(letra) != 1 or not letra.isalpha():
    print("Erro: Por favor, digite apenas uma única letra do alfabeto.")

elif letra in "aeiou":
    print(f"A letra '{entrada}' é uma VOGAL.")

else:
    print(f"A letra '{entrada}' é uma NÃO VOGAL (Consoante).")
