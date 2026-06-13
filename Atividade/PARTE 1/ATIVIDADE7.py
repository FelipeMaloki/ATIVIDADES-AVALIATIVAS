print("CADASTRE O ALUNO")

aluno = {}
aluno['nome'] = input("Digite o nome do aluno: ")
aluno['idade'] = int(input("Digite a idade do aluno: "))
aluno['curso'] = input("Digite o curso do aluno: ")

print("\nInformações do Aluno cadastrado:")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Curso: {aluno['curso']}")
