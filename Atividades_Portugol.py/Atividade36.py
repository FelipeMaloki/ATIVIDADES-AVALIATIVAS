print("=== JOGO DA ADIVINHAÇÃO ===")

palpite = int(input("Quantas bolinhas de gude estão no pote de vidro?: "))

if palpite == 82:
    print("Parabéns, você acertou!")

elif palpite < 82:
    print("Você errou! Existem mais bolinhas do que você digitou.")

else:
    print("Você errou! Existem menos bolinhas do que você digitou.")
