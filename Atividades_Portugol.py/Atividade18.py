print("=== SISTEMA DE TRIAGEM E ATENDIMENTO ===")


resposta = input("Você precisa de atendimento prioritário? (sim/não): ")


resposta_2 = resposta.strip().lower()

print("\n----------------------------------------")

if resposta_2 == "sim":
    print("Direcionamento: Vá para os caixas 1, 2 e 3.")
else:
    print("Direcionamento: Vá para qualquer caixa, exceto os 1, 2 e 3, que são prioritários.")
print("----------------------------------------")
