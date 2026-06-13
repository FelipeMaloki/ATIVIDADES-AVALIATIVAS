print("=== SISTEMA DE TELEMETRIA - KART ===")

soma_tempos = 0
total_pilotos = 0


continuar = "S"

while continuar == "S":

    nome = input("\nDigite o nome do piloto: ").strip()
    tempo_volta = float(input(f"Digite o tempo da volta de {nome} (em segundos): "))

    soma_tempos += tempo_volta
    total_pilotos += 1

    if total_pilotos == 1:
        nome_mais_rapido = nome
        tempo_mais_rapido = tempo_volta
        
        nome_mais_lento = nome
        tempo_mais_lento = tempo_volta
    else:
        if tempo_volta < tempo_mais_rapido:
            tempo_mais_rapido = tempo_volta
            nome_mais_rapido = nome

        if tempo_volta > tempo_mais_lento:
            tempo_mais_lento = tempo_volta
            nome_mais_lento = nome

    continuar = input("Deseja cadastrar outro piloto? (S/N): ").strip().upper()

if total_pilotos > 0:
    media_geral = soma_tempos / total_pilotos

    print("\n=========================================")
    print("         CLASSIFICAÇÃO DO TREINO         ")
    print("=========================================")
    print(f"Piloto mais RÁPIDO: {nome_mais_rapido} ({tempo_mais_rapido:.2f}s)")
    print(f"Piloto mais LENTO:  {nome_mais_lento} ({tempo_mais_lento:.2f}s)")
    print(f"Média de tempo de todas as voltas: {media_geral:.2f}s")
    print(f"Total de pilotos avaliados: {total_pilotos}")
    print("=========================================")
else:
    print("\nNenhum piloto foi cadastrado no sistema.")
