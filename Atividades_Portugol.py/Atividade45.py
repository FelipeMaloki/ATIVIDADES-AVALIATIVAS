print("=== CADASTRO DE SENHA SEGURA ===")
print("Regras: A senha deve ter exatamente 6 caracteres e conter APENAS vogais.")
print("=====================================================================")

senha_original = []

while len(senha_original) < 6:
    posicao = len(senha_original) + 1
    caractere = input(f"Digite o {posicao}º caractere da senha: ").strip().lower()
    
    
    if len(caractere) != 1 or caractere not in "aeiou":
        print("❌ Caractere inválido! Digite apenas uma única vogal (a, e, i, o ou u).\n")
    else:
        senha_original.append(caractere)

texto_original = ""
texto_criptografado = ""

for letra in senha_original:

    texto_original = texto_original + letra

    if letra == 'a':
        texto_criptografada_caractere = 'z'
    elif letra == 'e':
        texto_criptografada_caractere = '3'
    elif letra == 'i':
        texto_criptografada_caractere = 'l'
    elif letra == 'o':
        texto_criptografada_caractere = '0'
    elif letra == 'u':
        texto_criptografada_caractere = '$'
        
    texto_criptografado = texto_criptografado + texto_criptografada_caractere


print("\n=========================================")
print("          PROCESSO DE SEGURANÇA          ")
print("=========================================")
print(f"Senha digitada original:    {texto_original}")
print(f"Senha após criptografia:    {texto_criptografado}")
print("=========================================")
