print("=== SISTEMA DE VERIFICAÇÃO - CNH CATEGORIA D ===")

idade = int(input("Digite a sua idade: "))

print("\nCategorias permitidas para transição: B ou C")
categoria_atual = input("Qual é a sua categoria atual de CNH?: ").strip().upper()
anos_experiencia = int(input(f"Há quantos anos inteiros você possui a categoria {categoria_atual}?: "))

print("\nHistórico de conduta:")
infracoes_12_meses = input("Você cometeu alguma infração de trânsito nos últimos 12 meses? (S/N): ").strip().upper()

atende_idade = idade >= 21

atende_experiencia = (categoria_atual == "B" and anos_experiencia >= 2) or (categoria_atual == "C" and anos_experiencia >= 1)

atende_historico = infracoes_12_meses == "N"

print("\n=============================================")
print("            RESULTADO DA ANÁLISE             ")
print("=============================================")

if atende_idade and atende_experiencia and atende_historico:
    print("STATUS: CANDIDATO APTO!")
    print("O motorista cumpre todos os requisitos para iniciar o processo da categoria D.")
else:
    print("STATUS: CANDIDATO INAPTO.")
    print("Motivo(s) da recusa:")
    if not atende_idade:
        print("- A idade mínima exigida é de 21 anos.")
    if not atende_experiencia:
        print("- Tempo de habilitação insuficiente na categoria B (mínimo 2 anos) ou C (mínimo 1 ano).")
    if not atende_historico:
        print("- Não é permitido ter cometido infrações nos últimos 12 meses.")

print("=============================================")
