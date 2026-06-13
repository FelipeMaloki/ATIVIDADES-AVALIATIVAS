print("=== CONSULTA DE TAMANHOS DE BLUSAS ===")
print("Tamanhos disponíveis: P | M | G")
print("=======================================")

entrada = input("Digite o tamanho da blusa desejado: ")

tamanho = entrada.strip().upper()

print("\n-----------------------------------------")

if tamanho == "P":
    print("Tamanho P solicitado.")
    print("Dimensões: 0.46m x 0.55m")
elif tamanho == "M":
    print("Tamanho M solicitado.")
    print("Dimensões: 0.51m x 0.56m")
elif tamanho == "G":
    print("Tamanho G solicitado.")
    print("Dimensões: 0.52m x 0.58m")
else:
    print("Erro: Tamanho inválido! Por favor, escolha entre P, M ou G.")

print("-----------------------------------------")
