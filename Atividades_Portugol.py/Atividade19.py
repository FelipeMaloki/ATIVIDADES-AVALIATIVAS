# Cabeçalho do sistema
print("=== CALCULADORA DE COMBUSTÍVEL: ETANOL OU GASOLINA ===")

preco_gasolina = float(input("Digite o preço do litro da gasolina (R$): "))
preco_etanol = float(input("Digite o preço do litro do etanol (R$): "))

proporcao = preco_etanol / preco_gasolina

print("\n=========================================")
print(f"Resultado da proporção: {proporcao:.2f}")
print("-----------------------------------------")

if proporcao >= 0.7:
    print("Recomendação: Compensa abastecer com GASOLINA.")
else:
    print("Recomendação: Compensa abastecer com ETANOL.")

print("=========================================")
