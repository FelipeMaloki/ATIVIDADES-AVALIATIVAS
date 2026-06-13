nomes = []
for i in range(1, 6):
        nome = input(f"Digite o {i}º nome para cadastro: ")
        nomes.append(nome)
        
print("Nomes cadastrados na lista:")
for nome in nomes:
    print(f"- {nome}")