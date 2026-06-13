print("=== PROGRAMA DE FIDELIZAÇÃO: CARTELA DIGITAL ===")
print("Regra: A cada 10 refeições pagas, a próxima é por nossa conta!")
print("===============================================================")

cartela_fidelidade = []

while len(cartela_fidelidade) < 10:

    posicao_atual = len(cartela_fidelidade) + 1

    valor_gasto = float(input(f"Digite o valor do {posicao_atual}º almoço (R$): "))

    cartela_fidelidade.append(valor_gasto)

    print(f"-> Sucesso! Posição {posicao_atual}/10 preenchida.")
    print(f"-> Histórico atual de gastos: {cartela_fidelidade}\n")

print("===============================================================")
print("  HOJE O SEU ALMOÇO É UMA CORTESIA DA CASA, PARABÉNS!  ")
print("===============================================================")
