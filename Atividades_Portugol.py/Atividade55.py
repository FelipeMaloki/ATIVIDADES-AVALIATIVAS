# --- FUNÇÃO 1: REAJUSTE DA GASOLINA ---
def reajustar_gasolina(combustiveis, valor_reajuste):
    
    combustiveis["gasolina"] += valor_reajuste


# --- FUNÇÃO 2: REAJUSTE DO ETANOL ---
def reajustar_etanol(combustiveis, valor_reajuste):
    
    combustiveis["etanol"] += valor_reajuste
    
    
    impacto_gasolina = valor_reajuste * 0.27
    combustiveis["gasolina"] += impacto_gasolina


print("=== SISTEMA DE REAJUSTE DE COMBUSTÍVEIS ===")

preco_gasolina_atual = float(input("Digite o preço atual da gasolina (R$): "))
preco_etanol_atual = float(input("Digite o preço atual do etanol (R$): "))

precos_posto = {
    "gasolina": preco_gasolina_atual,
    "etanol": preco_etanol_atual
}

valor_do_reajuste = float(input("Digite o valor do reajuste (R$): "))

tipo_combustivel = ""
while tipo_combustivel not in ["G", "E"]:
    tipo_combustivel = input("Qual o combustível do reajuste? (G - Gasolina / E - Etanol): ").strip().upper()
    if tipo_combustivel not in ["G", "E"]:
        print(" Entrada inválida! Digite apenas 'G' para Gasolina ou 'E' para Etanol.\n")

if tipo_combustivel == "G":
    reajustar_gasolina(precos_posto, valor_do_reajuste)
    print("\n-> Aplicando reajuste exclusivo na Gasolina...")
elif tipo_combustivel == "E":
    reajustar_etanol(precos_posto, valor_do_reajuste)
    print("\n-> Aplicando reajuste no Etanol com reflexo de 27% na Gasolina...")

print("\n=========================================")
print("          NOVOS PREÇOS DA BOMBA          ")
print("=========================================")
print(f"Preço Final da Gasolina:  R$ {precos_posto['gasolina']:.2f}")
print(f"Preço Final do Etanol:    R$ {precos_posto['etanol']:.2f}")
print("=========================================")
