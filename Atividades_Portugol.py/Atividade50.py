def somar(a, b):
    resultado = a + b
    print(f"\n✨ Resultado da Soma: {a} + {b} = {resultado}")

def subtrair(a, b):
    resultado = a - b
    print(f"\n✨ Resultado da Subtração: {a} - {b} = {resultado}")

def multiplicar(a, b):
    resultado = a * b
    print(f"\n✨ Resultado da Multiplicação: {a} * {b} = {resultado}")

def dividir(a, b):
    # Validação para evitar o erro de divisão por zero
    if b == 0:
        print("\n Erro: Não é possível dividir um número por zero!")
    else:
        resultado = a / b
        print(f"\n✨ Resultado da Divisão: {a} / {b} = {resultado}")


opcao = 0


while opcao != 5:
    print("\n=========================================")
    print("          CALCULADORA EM PYTHON          ")
    print("=========================================")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair do programa")
    print("=========================================")
    
    opcao = int(input("Escolha a operação desejada (1-5): "))
    
    if 1 <= opcao <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        
        if opcao == 1:
            somar(num1, num2)
        elif opcao == 2:
            subtrair(num1, num2)
        elif opcao == 3:
            multiplicar(num1, num2)
        elif opcao == 4:
            dividir(num1, num2)
            
    elif opcao == 5:
        print("\nEncerrando a calculadora. Até logo!")
    else:
        print("\n Opção inválida! Escolha um número de 1 a 5.")
