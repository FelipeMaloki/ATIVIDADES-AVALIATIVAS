def mmc(a, b):
    maior = max(a, b)
    
    while True:
        if maior % a == 0 and maior % b == 0:
            return maior
        maior += 1

print(mmc(12, 18))  
