def entrega_3_dias(valor_base):
    return valor_base + 25.00

def entrega_5_dias(valor_base):
    return valor_base + 20.00

def entrega_7_dias(valor_base):
    return valor_base + 15.00

def entrega_10_dias(valor_base):
    return valor_base + 10.00

print("=== SIMULADOR DE FRETE - SEBO ONLINE ===")

valor_pedido = float(input("Digite o valor total dos livros (R$): "))

print("\nOpções de prazos de entrega:")
print("Opção [3]  - 3 dias úteis  (Frete: R$ 25,00)")
print("Opção [5]  - 5 dias úteis  (Frete: R$ 20,00)")
print("Opção [7]  - 7 dias úteis  (Frete: R$ 15,00)")
print("Opção [10] - 10 dias úteis (Frete: R$ 10,00)")

prazo_escolhido = 0
prazos_validos = [3, 5, 7, 10]

while prazo_escolhido not in prazos_validos:
    prazo_escolhido = int(input("\nInforme o prazo desejado (3, 5, 7 ou 10): "))
    
    if prazo_escolhido not in prazos_validos:
        print(" Opção inválida! Escolha apenas um dos prazos listados acima.")

if prazo_escolhido == 3:
    valor_final = entrega_3_dias(valor_pedido)
elif prazo_escolhido == 5:
    valor_final = entrega_5_dias(valor_pedido)
elif prazo_escolhido == 7:
    valor_final = entrega_7_dias(valor_pedido)
elif prazo_escolhido == 10:
    valor_final = entrega_10_dias(valor_pedido)

custo_frete = valor_final - valor_pedido

print("\n=========================================")
print("          FECHAMENTO DO PEDIDO           ")
print("=========================================")
print(f"Valor dos Livros:       R$ {valor_pedido:.2f}")
print(f"Prazo Selecionado:      {prazo_escolhido} dias úteis")
print(f"Custo do Frete:         R$ {custo_frete:.2f}")
print("-----------------------------------------")
print(f"TOTAL COM FRETE:        R$ {valor_final:.2f}")
print("=========================================")
