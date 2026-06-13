

def exercicio_for():
    print("A MÉDIA DO ALUNO")
    soma = 0
    for i in range(1, 6):
        num = float(input(f"Digite a {i}º nota do aluno: "))
        soma += num
    
    media = soma / 5
    print(f"Soma total: {soma} | Média dos números: {media}")


def exercicio_condicional():
    print("SITUAÇÃO DO ALUNO")
    
    nota = float(input("Digite a nota do aluno (0 a 10): "))
    
    if nota >= 7.0:
        print("Situação: Aprovado")
    elif 5.0 <= nota < 7.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

def exercicio_dicionarios():
    print("CADASTRE O ALUNO")
    
    aluno = {}
    aluno['nome'] = input("Digite o nome do aluno: ")
    aluno['idade'] = int(input("Digite a idade do aluno: "))
    aluno['curso'] = input("Digite o curso do aluno: ")
    
    print("\nInformações do Aluno cadastrado:")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")
    print(f"Curso: {aluno['curso']}")


def calcular_media(nota1, nota2):
    # Função auxiliar solicitada no item 8
    return (nota1 + nota2) / 2

def exercicio_funcoes():
    print("\n--- 8. Funções ---")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    
    media_final = calcular_media(n1, n2)
    print(f"A média retornada pela função é: {media_final}")

def exercicio_listas():

    nomes = []
    for i in range(1, 6):
        nome = input(f"Digite o {i}º nome para cadastro: ")
        nomes.append(nome)
        
    print("Nomes cadastrados na lista:")
    for nome in nomes:
        print(f"- {nome}")

def exercicio_arquivo_txt():
    
    nome_aluno = input("Digite o nome do aluno para salvar no arquivo: ")
    
    save= open("c:/Users/Maloki/Documents/Cadastro_de_alunos.txt","a", encoding='utf-8')

    save.write(nome_aluno + "\n")
        
    print("Informação gravada com sucesso no arquivo")

def exercicio_matrizes():
    
    matriz = []
    soma_elementos = 0
    diagonal_principal = []
    
    
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
            soma_elementos += valor
            if i == j:
                diagonal_principal.append(valor)
        matriz.append(linha)
        
    print("\nVisualização da Matriz 3x3:")
    for linha in matriz:
        print(linha)
        
    print(f"\nSoma de todos os elementos: {soma_elementos}")
    print(f"Elementos da diagonal principal: {diagonal_principal}")

def exercicio_while():
    
    soma = 0
    quantidade = 0
    
    while True:
        num = float(input("Digite um número (ou 0 para sair): "))
        if num == 0:
            break
        soma += num
        quantidade += 1
        
    print(f"Quantidade de números digitados: {quantidade} | Soma total: {soma}")

def exercicio_tuplas():
    
    meses = (
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    )
    
    opcao = int(input("Digite o número do mês (1 a 12): "))
    
    if 1 <= opcao <= 12:
        
        print(f"O mês correspondente é: {meses[opcao - 1]}")
    else:
        print("Número inválido! Digite um valor entre 1 e 12.")


if __name__ == "__main__":

    exercicio_for()
    exercicio_condicional()
    exercicio_while()
    exercicio_listas()
    exercicio_tuplas()
    exercicio_dicionarios()
    exercicio_funcoes()
    exercicio_arquivo_txt()
    exercicio_matrizes()


