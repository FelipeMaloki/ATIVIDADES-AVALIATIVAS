print("=== SISTEMA DE CAIXA - PADARIA ===")

PRECO_PAO = 0.50
PRECO_QUEIJO = 12.00
PRECO_BISNAGA = 4.50
PRECO_PAO_FORMA = 7.50
PRECO_LEITE = 5.00
PRECO_PAO_DOCE = 1.50
PRECO_SUSPIRO = 3.00

print("\nPor favor, informe a quantidade de cada produto comprado:")
qtd_pao = int(input("Quantidade de Pães: "))
qtd_queijo = int(input("Quantidade de Queijos: "))
qtd_bisnaga = int(input("Quantidade de Bisnagas: "))
qtd_pao_forma = int(input("Quantidade de Pães de Forma: "))
qtd_leite = int(input("Quantidade de Leites: "))
qtd_pao_doce = int(input("Quantidade de Pães Doces: "))
qtd_suspiro = int(input("Quantidade de Suspiros: "))

valor_bruto = (
    (qtd_pao * PRECO_PAO) +
    (qtd_queijo * PRECO_QUEIJO) +
    (qtd_bisnaga * PRECO_BISNAGA) +
    (qtd_pao_forma * PRECO_PAO_FORMA) +
    (qtd_leite * PRECO_LEITE) +
    (qtd_pao_doce * PRECO_PAO_DOCE) +
    (qtd_suspiro * PRECO_SUSPIRO)
)

desconto_regra1 = 0.0
desconto_regra2 = 0.0
desconto_regra3 = 0.0

if qtd_pao >= 10 and qtd_queijo >= 1:
    desconto_regra1 = 0.10

if qtd_bisnaga >= 1 or qtd_pao_forma >= 1:
    desconto_regra2 = 0.15

if qtd_leite >= 1 and (qtd_pao_doce >= 1 or qtd_suspiro >= 1):
    desconto_regra3 = 0.05

maior_desconto = max(desconto_regra1, desconto_regra2, desconto_regra3)

valor_desconto = valor_bruto * maior_desconto
valor_final = valor_bruto - valor_desconto

print("\n=========================================")
print("              CUPOM FISCAL               ")
print("=========================================")
print(f"Valor Total Bruto:       R$ {valor_bruto:.2f}")
print(f"Percentual de Desconto:  {maior_desconto * 100:.0f}%")
print(f"Valor descontado:        R$ {valor_desconto:.2f}")
print("-----------------------------------------")
print(f"VALOR TOTAL A PAGAR:     R$ {valor_final:.2f}")
print("=========================================")
