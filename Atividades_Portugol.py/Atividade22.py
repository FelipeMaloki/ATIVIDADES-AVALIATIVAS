print("=== MENU DE SUCOS DA LOJA ===")
print("L - Laranja")
print("M - Morango")
print("A - Acerola")
print("U - Uva")
print("=============================")

opcao = input("Digite a letra correspondente ao suco desejado: ")

opcao_ajustada = opcao.strip().upper()

print("\n-----------------------------------------")

if opcao_ajustada == "L":
    print("Suco Escolhido: Laranja")
    print("Principal Vitamina fornecida: Vitamina C")
elif opcao_ajustada == "M":
    print("Suco Escolhido: Morango")
    print("Principal Vitamina fornecida: Vitamina A")
elif opcao_ajustada == "A":
    print("Suco Escolhido: Acerola")
    print("Principal Vitamina fornecida: Vitamina C")
elif opcao_ajustada == "U":
    print("Suco Escolhido: Uva")
    print("Principal Vitamina fornecida: Vitamina E")
else:
    print("Erro: Opção inválida! Por favor, escolha L, M, A ou U.")

print("-----------------------------------------")
