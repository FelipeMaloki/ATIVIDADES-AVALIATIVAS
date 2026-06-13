print("=== SISTEMA DE VENDAS: VIAÇÃO PYTHON ===")

poltronas_disponiveis = list(range(1, 43))

while len(poltronas_disponiveis) > 0:
    
    
    print("\n--------------------------------------------------")
    print("POLTRONAS DISPONÍVEIS PARA VENDA:")
    print(poltronas_disponiveis)
    print("--------------------------------------------------")
    
    
    escolha = int(input("Digite o número da poltrona desejada (ou 0 para fechar o sistema): "))
    
    
    if escolha == 0:
        print("\nFechando o sistema de vendas...")
        break
        
    
    if escolha in poltronas_disponiveis:
        
        poltronas_disponiveis.remove(escolha)
        print(f" Sucesso! Poltrona {escolha} reservada com segurança.")
    else:
        
        if escolha < 1 or escolha > 42:
            print(" Erro: Essa poltrona não existe! Escolha um número de 1 a 42.")
        else:
            print(" Erro: Essa poltrona já foi vendida! Escolha outro lugar.")

if len(poltronas_disponiveis) == 0:
    print("\n Lotação máxima atingida! Todos os 42 assentos foram vendidos.")
print("=== FIM DO EXPEDIENTE ===")
