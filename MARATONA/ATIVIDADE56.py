def maior_sequencia(texto):
    if not texto:
        return ""
        
    sequencia_atual = texto[0]
    maior_seq = texto[0]
    
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            sequencia_atual += texto[i]
        else:
            sequencia_atual = texto[i]
        if len(sequencia_atual) > len(maior_seq):
            maior_seq = sequencia_atual
            
    return maior_seq

print(maior_sequencia("aabbccdddde")) 
print(maior_sequencia("aaabbbcccc"))   