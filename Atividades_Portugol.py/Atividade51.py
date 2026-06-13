def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("\n Aviso: Não é possível dividir por zero! O resultado da divisão foi definido como 0.")
        return 0.0
    return a / b


print("=========================================")
print("     CALCULADORA DE OPERAÇÕES SIMULTÂNEAS ")
print("=========================================")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado_soma = somar(num1, num2)
resultado_subtracao = subtrair(num1, num2)
resultado_multiplicacao = multiplicar(num1, num2)
resultado_divisao = dividir(num1, num2)

soma_dos_retornos = resultado_soma + resultado_subtracao + resultado_multiplicacao + resultado_divisao

print("\n=========================================")
print("          RESULTADOS DETALHADOS          ")
print("=========================================")
print(f"1. Resultado da Soma:          {resultado_soma}")
print(f"2. Resultado da Subtração:     {resultado_subtracao}")
print(f"3. Resultado da Multiplicação: {resultado_multiplicacao}")
print(f"4. Resultado da Divisão:       {resultado_divisao}")
print("-----------------------------------------")
print(f"SOMA TOTAL DOS RETORNOS:       {soma_dos_retornos}")
print("=========================================")
