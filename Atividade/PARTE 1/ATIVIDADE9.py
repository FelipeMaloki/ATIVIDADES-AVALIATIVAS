nome_aluno = input("Digite o nome do aluno para salvar no arquivo: ")
    
save= open("c:/Users/Maloki/Documents/Cadastro_de_alunos.txt","a", encoding='utf-8')

save.write(nome_aluno + "\n")
        
print("Informação gravada com sucesso no arquivo")