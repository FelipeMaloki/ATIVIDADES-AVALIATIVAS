
nomes = []
idades = []
turmas = []
matriz_notas = []  

def cadastrar_aluno():
    print("\n--- CADASTRAR ALUNO ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    turma = input("Turma: ")
    
    nomes.append(nome)
    idades.append(idade)
    turmas.append(turma)
    matriz_notas.append([0.0, 0.0, 0.0, 0.0]) 
    print("Aluno cadastrado com sucesso!")

def lancar_notas():
    print("\n--- LANÇAR NOTAS ---")
    if len(nomes) == 0:
        print("Nenhum aluno cadastrado.")
        return 
        
    
    for i in range(len(nomes)):
        print(f"[{i}] {nomes[i]}")
        
    indice = int(input("Digite o número do aluno: "))
    
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    
    
    matriz_notas[indice] = [n1, n2, n3, n4]
    print("Notas lançadas com sucesso!")

def consultar_aluno():
    print("\n--- CONSULTAR ALUNO ---")
    busca = input("Nome do aluno para buscar: ")
    encontrado = False
    
    for i in range(len(nomes)):
        if busca.lower() in nomes[i].lower():
            encontrado = True
            notas = matriz_notas[i]
            media = sum(notas) / 4
            
            
            if media >= 7:
                situacao = "Aprovado"
            elif media >= 5:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"
                
            print(f"\nNome: {nomes[i]} | Idade: {idades[i]} | Turma: {turmas[i]}")
            print(f"Notas: {notas} | Média Autocalculada: {media:.1f} | Situação: {situacao}")
            
    if not encontrado:
        print("Aluno não encontrado.")

def relatorio_geral():
    print("\n--- RELATÓRIO GERAL ---")
    total = len(nomes)
    if total == 0:
        print("Sem dados no sistema.")
        return
        
    soma_medias = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    
    melhor_aluno = ""
    maior_media = -1
    pior_aluno = ""
    menor_media = 11

    for i in range(total):
        media = sum(matriz_notas[i]) / 4
        soma_medias += media
        
        if media >= 7:
            aprovados += 1
        elif media >= 5:
            recuperacao += 1
        else:
            reprovados += 1
            
        
        if media > maior_media:
            maior_media = media
            melhor_aluno = nomes[i]
        if media < menor_media:
            menor_media = media
            pior_aluno = nomes[i]

    print(f"Quantidade de alunos: {total}")
    print(f"Média da turma: {soma_medias / total:.1f}")
    print(f"Melhor aluno: {melhor_aluno} (Média: {maior_media:.1f})")
    print(f"Pior aluno: {pior_aluno} (Média: {menor_media:.1f})")
    print(f"Aprovados: {aprovados} | Recuperação: {recuperacao} | Reprovados: {reprovados}")

def salvar_dados():
    print("\n--- SALVAR DADOS ---")
    arquivo = open("c:/Users/Maloki/Documents/Cadastro_de_alunos_PT2.txt","w", encoding='utf-8')
    for i in range(len(nomes)):
        media = sum(matriz_notas[i]) / 4
        linha = f"Aluno: {nomes[i]}, Turma: {turmas[i]}, Média: {media:.1f}\n"
        arquivo.write(linha)
    arquivo.close()
    print("Dados salvos com sucesso no arquivo")

def menu():
    while True:
        print("\n==============================")
        print("  SISTEMA ESCOLAR  ")
        print("==============================")
        print("1. Cadastrar Aluno")
        print("2. Lançar Notas")
        print("3. Consultar Aluno")
        print("4. Relatório Geral")
        print("5. Salvar Dados")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            lancar_notas()
        elif opcao == "3":
            consultar_aluno()
        elif opcao == "4":
            relatorio_geral()
        elif opcao == "5":
            salvar_dados()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")


menu()
