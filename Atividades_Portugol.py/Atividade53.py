# --- DEFINIÇÃO DA FUNÇÃO DE GRATIFICAÇÃO ---
def calcular_e_mostrar_gratificacao(salario_base, mes_simulado):
    
    grupo_30_porcento = ["janeiro", "fevereiro", "marco", "abril", "maio"]
    grupo_40_porcento = ["junho", "julho", "agosto", "setembro", "outubro", "novembro"]
    
    if mes_simulado in grupo_30_porcento:
        porcentagem = 30
        gratificacao = salario_base * 0.30
    elif mes_simulado in grupo_40_porcento:
        porcentagem = 40
        gratificacao = salario_base * 0.40
    elif mes_simulado == "dezembro":
        porcentagem = 60
        gratificacao = salario_base * 0.60
    else:
        print("\n❌ Erro: Mês incorreto! Não foi possível calcular a gratificação.")
        return 
        
    
    salario_total = salario_base + gratificacao
    print("\n=========================================")
    print("        RESULTADO DA SIMULAÇÃO           ")
    print("=========================================")
    print(f"Mês Simulado:          {mes_simulado.capitalize()}")
    print(f"Salário Básico:        R$ {salario_base:.2f}")
    print(f"Gratificação ({porcentagem}%):    R$ {gratificacao:.2f}")
    print("-----------------------------------------")
    print(f"SALÁRIO TOTAL NO MÊS:  R$ {salario_total:.2f}")
    print("=========================================")


print("=== SIMULADOR DE GRATIFICAÇÃO - VEÍCULOS ===")

salario = float(input("Digite o salário básico do funcionário (R$): "))

mes = input("Digite o mês que deseja simular (ex: Janeiro, Março): ").strip().lower()


if mes == "março":
    mes = "marco"

calcular_e_mostrar_gratificacao(salario, mes)
