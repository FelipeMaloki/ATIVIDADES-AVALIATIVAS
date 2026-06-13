print("=== CADASTRO DA AGÊNCIA ESPACIAL PYTHON ===")

nome_astronauta = input("Digite o nome ou codinome do Astronauta: ")

anos_treinamento = int(input("Quantos anos inteiros de treinamento você possui? "))

distancia_destino = float(input("Distância do planeta de destino : "))

resposta_combustivel = input("O tanque de combustível está totalmente cheio? (S/N): ").upper()
tanque_pronto = resposta_combustivel == "S"

print("\n=============================================")
print("          DADOS DO TRIPULANTE SALVOS         ")
print("=============================================")

print(f"Nome do Astronauta: {nome_astronauta}")
print(f"Tempo de Treinamento: {anos_treinamento} anos")
print(f"Distância da Missão: {distancia_destino} anos-luz")
print(f"Nave Pronta para Decolagem?: {tanque_pronto}")

print("=============================================")
print("Missão autorizada! Boa viagem pelo espaço!")
