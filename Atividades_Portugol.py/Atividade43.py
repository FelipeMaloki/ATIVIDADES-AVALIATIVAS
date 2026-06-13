print("=== TELEMETRIA DE KART: HISTÓRICO DE VOLTAS ===")

velocidades = []

for i in range(1, 7):
    velocidade = float(input(f"Digite a velocidade da {i}ª volta (em km/h): "))
    velocidades.append(velocidade)  

velocidades_invertidas = velocidades[::-1]

print("\n=========================================")
print("          RELATÓRIO DE VELOCIDADES       ")
print("=========================================")
print("Ordem lida original:", velocidades)
print("-----------------------------------------")
print("Ordem INVERSA (Última para a Primeira):")

for indice, vel in enumerate(velocidades_invertidas, start=1):
    print(f"Exibição {indice}: {vel} km/h")

print("=========================================")
