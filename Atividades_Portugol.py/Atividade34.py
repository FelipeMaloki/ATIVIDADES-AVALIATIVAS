print("=== CONTROLE DE ALTURA DE ATLETAS ===")

atletas_altos = 0

for i in range(1, 13):
    altura = float(input(f"Digite a altura do {i}º atleta (ex: 1.95): "))
    
    
    if altura > 1.90:
        atletas_altos = atletas_altos + 1

print("\n=========================================")
print("           RELATÓRIO DA EQUIPE           ")
print("=========================================")
print(f"Total de atletas com mais de 1.90m: {atletas_altos}")
print("=========================================")
