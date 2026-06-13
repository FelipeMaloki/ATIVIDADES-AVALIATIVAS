print("=== GERADOR DE PALAVRAS POR VOGAL ===")
print("Vogais disponíveis: A, E, I, O, U")
print("=====================================")

entrada = input("Digite uma vogal: ")

vogal = entrada.strip().lower()

print("\n-----------------------------------------")

if vogal == "a":
    print("Palavras com A: Amor, Abacaxi, Aventura, Azul, Amizade.")
elif vogal == "e":
    print("Palavras com E: Estrela, Elefante, Escola, Energia, Esperança.")
elif vogal == "i":
    print("Palavras com I: Igreja, Ilha, Ímã, Ideia, Inovação.")
elif vogal == "o":
    print("Palavras com O: Olho, Ouro, Oceano, Orquestra, Otimismo.")
elif vogal == "u":
    print("Palavras com U: Uva, Urso, Universo, Urgência, Único.")
else:
    print("Erro: Entrada inválida! Certifique-se de digitar apenas UMA vogal (A, E, I, O ou U).")

print("-----------------------------------------")
