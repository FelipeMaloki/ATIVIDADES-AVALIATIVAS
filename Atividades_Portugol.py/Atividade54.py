# --- DEFINIÇÃO DA FUNÇÃO COM PASSAGEM POR REFERÊNCIA ---
def calcular_gratificacao_por_referencia(dados_funcionario, mes_simulado):
    
    
    grupo_30_porcento = ["janeiro", "fevereiro", "marco", "abril", "maio"]
    grupo_40_porcento = ["junho", "julho", "agosto", "setembro", "outubro", "novembro"]
    
    
    if mes_simulado in grupo_30_porcento:
        dados_funcionario[1] = dados_funcionario[0] * 0.30
    elif mes_simulado in grupo_40_porcento:
        dados_funcionario[1] = dados_funcionario[0] * 0.40
    elif mes_simulado == "dezembro":
        dados_funcionario[1] = dados_funcionario[0] * 0.60
    else:
        print("\n Erro: Mês incorreto! Não foi possível calcular a gratificação.")
        return

print("=== SIMULADOR COM PASSAGEM POR REFERÊNCIA ===")

salario_inicial = float(input("Digite o salário básico do funcionário (R$): "))
mes = input("Digite o mês que deseja simular (ex: Janeiro, Março): ").strip().lower()

if mes == "março":
    mes = "marco"

ficha_financeira = [salario_inicial, 0.0]

print("\n--- Antes de chamar a função ---")
print(f"Lista original na memória: {ficha_financeira}")
print(f"Valor da Gratificação: R$ {ficha_financeira[1]:.2f}")

calcular_gratificacao_por_referencia(ficha_financeira, mes)

salario_total = ficha_financeira[0] + ficha_financeira[1]

print("\n--- Depois de chamar a função (Valores modificados por Referência) ---")
print(f"Lista modificada na memória: {ficha_financeira}")
print("=========================================")
print("        RESULTADO DA SIMULAÇÃO           ")
print("=========================================")
print(f"Mês Simulado:          {mes.capitalize()}")
print(f"Salário Básico:        R$ {ficha_financeira[0]:.2f}")
print(f"Gratificação Aplicada: R$ {ficha_financeira[1]:.2f}")
print("-----------------------------------------")
print(f"SALÁRIO TOTAL NO MÊS:  R$ {salario_total:.2f}")
print("=========================================")
