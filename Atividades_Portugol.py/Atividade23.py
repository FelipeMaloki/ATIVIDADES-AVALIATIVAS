print("=== CALENDÁRIO DAS ESTAÇÕES DO ANO ===")
print("Opções: Outono | Inverno | Primavera | Verão")
print("=======================================")

estacao = input("Digite o nome da estação para saber quando ela começa: ")

estacao_ajustada = estacao.strip().lower()

print("\n-----------------------------------------")

if estacao_ajustada == "outono":
    print("A estação do Outono começa no dia 20 de março.")
elif estacao_ajustada == "inverno":
    print("A estação do Inverno começa no dia 21 de junho.")
elif estacao_ajustada == "primavera":
    print("A estação da Primavera começa no dia 22 de setembro.")
elif estacao_ajustada == "verão" or estacao_ajustada == "verao":
    print("A estação do Verão começa no dia 21 de dezembro.")
else:
    print("Erro: Estação inválida! Por favor, digite Outono, Inverno, Primavera ou Verão.")

print("-----------------------------------------")
