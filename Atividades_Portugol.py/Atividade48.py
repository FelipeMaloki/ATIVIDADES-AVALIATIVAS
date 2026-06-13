print("=== SISTEMA DE ESTACIONAMENTO PRO ===")


estacionamento = [
    ["Livre", "Livre", "Livre", "Livre", "Livre", "Livre", "Livre", "Livre", "Livre"],
    ["Livre", "Livre", "Livre", "Livre", "Livre", "Livre", "Livre", "Livre", "Livre"]
]

opcao = 0


while opcao != 4:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Exibir Mapa de Vagas")
    print("2. Cadastrar Veículo (Entrada)")
    print("3. Liberar Vaga (Saída / Consulta)")
    print("4. Encerrar Sistema")
    
    opcao = int(input("Escolha uma opção: "))
    
    
    if opcao == 1:
        print("\n================ MAPA DE VAGAS ================")
        print("Lado Esquerdo:", estacionamento[0])
        print("Lado Direito: ", estacionamento[1])
        print("===============================================")
        
    
    elif opcao == 2:
        placa = input("\nDigite a placa do veículo: ").strip().upper()
        
        print("Selecione o setor da vaga:")
        print("0 - Lado Esquerdo")
        print("1 - Lado Direito")
        linha = int(input("Setor (0 ou 1): "))
        coluna = int(input("Número da vaga (1 a 9): ")) - 1 
        
        # Validação de limites da matriz
        if (linha == 0 or linha == 1) and (0 <= coluna <= 8):
            
            if estacionamento[linha][coluna] == "Livre":
                estacionamento[linha][coluna] = placa
                setor_nome = "Lado Esquerdo" if linha == 0 else "Lado Direito"
                print(f" Sucesso! Carro [{placa}] estacionado no {setor_nome}, Vaga {coluna + 1}.")
            else:
                print(" Erro: Esta vaga já está ocupada por outro veículo!")
        else:
            print(" Erro: Setor ou número de vaga inválido!")
            
    
    elif opcao == 3:
        placa_busca = input("\nDigite a placa do veículo para retirada: ").strip().upper()
        encontrado = False
        
        
        for l in range(2):
            for c in range(9):
                if estacionamento[l][c] == placa_busca:
                    encontrado = True
                    setor_nome = "Lado Esquerdo" if l == 0 else "Lado Direito"
                    
                    print(f" Veículo encontrado no índice da matriz: Linha {l}, Coluna {c}")
                    print(f" Localização física: {setor_nome}, Vaga {c + 1}.")
                    
                    
                    estacionamento[l][c] = "Livre"
                    print(f" Carro [{placa_busca}] liberado. Vaga desocupada com sucesso!")
                    break 
            if encontrado:
                break 
        if not encontrado:
            print(f" Erro: O veículo com a placa {placa_busca} não foi encontrado no estacionamento.")

print("\n=== SISTEMA ENCERRADO COM SEGURANÇA ===")
