meses = (
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    )
    
opcao = int(input("Digite o número do mês (1 a 12): "))
    
if 1 <= opcao <= 12:
        
        print(f"O mês correspondente é: {meses[opcao - 1]}")
else:
        print("Número inválido! Digite um valor entre 1 e 12.")