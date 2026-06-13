print("=== DESAFIO DAS BOLINHAS DE GUDE: MODO PROFISSIONAL ===")

total_tentativas = 0
erros_abaixo = 0
erros_acima = 0

jogar_novamente = "S"

while jogar_novamente == "S":
    entrada_usuario = input("\nQuantas bolinhas de gude estão no pote de vidro?: ").strip()
    
    if not entrada_usuario.isdigit():
        print("❌ Entrada inválida! Por favor, digite apenas números inteiros.")
        continue 

    palpite = int(entrada_usuario)
    total_tentativas += 1

    if palpite == 82:
        print(" Parabéns, você acertou o número exato!")
    elif palpite < 82:
        print(" Você errou! Existem MAIS bolinhas do que você digitou.")
        erros_abaixo += 1
    else:
        print(" Você errou! Existem MENOS bolinhas do que você digitou.")
        erros_acima += 1

    resposta = input("\nDeseja dar mais um palpite? (Sim/Não): ").strip().upper()
    jogar_novamente = resposta[0] if resposta else "N"

if erros_abaixo > erros_acima:
    erro_mais_comum = "Chutar números ABAIXO do valor real"
elif erros_acima > erros_abaixo:
    erro_mais_comum = "Chutar números ACIMA do valor real"
else:
    if erros_abaixo == 0 and erros_acima == 0:
        erro_mais_comum = "Nenhum (Você acertou de primeira!)"
    else:
        erro_mais_comum = "Empate (Errou a mesma quantidade para mais e para menos)"

print("\n==================================================")
print("               RELATÓRIO DO JOGO                  ")
print("==================================================")
print(f"Total de tentativas realizadas: {total_tentativas}")
print(f"Erros cometidos para baixo:     {erros_abaixo}")
print(f"Erros cometidos para cima:      {erros_acima}")
print(f"Seu erro mais comum foi:        {erro_mais_comum}")
print("==================================================")
print("Obrigado por jogar!")
