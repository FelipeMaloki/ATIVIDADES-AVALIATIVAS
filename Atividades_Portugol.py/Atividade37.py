print("=== JOGO DA ADIVINHAÇÃO COM REPETIÇÃO ===")

palpite = 0

while palpite != 82:

    palpite = int(input("\nQuantas bolinhas de gude estão no pote de vidro?: "))
    
    if palpite < 82:
        print("Você errou! Existem mais bolinhas do que você digitou. Tente de novo!")
        
    elif palpite > 82:
        print("Você errou! Existem menos bolinhas do que você digitou. Tente de novo!")

print("\n=========================================")
print("   Parabéns, você acertou o número!   ")
print("=========================================")
