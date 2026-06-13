quantidade = int(input("Digite a quantidade de sucos desejada: "))

if quantidade > 10:
    preco_unitario = 4.50
else:
    preco_unitario = 5.50

valor_total = quantidade * preco_unitario

print("\n=========================================")
print("            LOJA DE SUCOS                ")
print("=========================================")
print(f"Quantidade comprada: {quantidade} unidades")
print(f"Preço por unidade: R$ {preco_unitario:.2f}")
print("-----------------------------------------")
print(f"VALOR TOTAL A PAGAR: R$ {valor_total:.2f}")
print("=========================================")
