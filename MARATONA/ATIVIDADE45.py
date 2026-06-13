def romano_para_inteiro(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    comprimento = len(romano)
    
    for i in range(comprimento):
        valor_atual = valores[romano[i]]
        
        if i + 1 < comprimento and valor_atual < valores[romano[i + 1]]:
            total -= valor_atual
        else:
            total += valor_atual
            
    return total

print(romano_para_inteiro("XIV"))  
