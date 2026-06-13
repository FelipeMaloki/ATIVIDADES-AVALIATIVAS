print("=== CONTROLE DE ARTILHARIA DO TIME ===")

for i in range(1, 12):
    print(f"\n--- Cadastro do {i}º Jogador ---")
    nome = input("Digite o nome do jogador: ").strip()
    gols = int(input(f"Quantos gols {nome} marcou no campeonato?: "))
    
    
    if i == 1:
        artilheiro_nome = nome
        artilheiro_gols = gols
    else:
        if gols > artilheiro_gols:
            artilheiro_gols = gols
            artilheiro_nome = nome

print("\n=========================================")
print("          PRÊMIO CHUTEIRA DE OURO        ")
print("=========================================")
print(f"Artilheiro do time: {artilheiro_nome}")
print(f"Total de gols marcados: {artilheiro_gols} gols")
print("=========================================")
