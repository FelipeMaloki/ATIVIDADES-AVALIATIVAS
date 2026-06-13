print("=== CONTADOR DE NÚMEROS MAIORES QUE 50 ===")

contador_maiores = 0

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    
    
    if numero > 50:
        contador_maiores = contador_maiores + 1

print("\n=========================================")
print(f"Total de números maiores que 50: {contador_maiores}")
print("=========================================")
