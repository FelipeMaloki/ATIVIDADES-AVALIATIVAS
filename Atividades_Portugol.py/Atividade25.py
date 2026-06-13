print("=== CALCULADORA DE IMC ===")

peso = float(input("Digite o seu peso (em kg, ex: 75.5): "))
altura = float(input("Digite a sua altura (em metros, ex: 1.75): "))

imc = peso / (altura * altura)

print("\n=========================================")
print(f"Seu IMC calculado é: {imc:.1f}")
print("-----------------------------------------")

if imc < 18.5:
    print("Classificação: Magreza")
elif 18.5 <= imc <= 24.9:
    print("Classificação: Normal")
elif 24.9 < imc <= 30.0:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

print("=========================================")
