passos_detalhados = [
    "1. Entrada: O usuário digita a URL (ex: ://google.com) e pressiona Enter.",
    "2. Consulta DNS: O computador pergunta ao Servidor DNS: 'Qual é o número de IP deste site?'.",
    "3. Tradução: O DNS responde com o endereço IP real.",
    "4. Conexão: O navegador envia um pedido (HTTP/HTTPS) para o servidor que guarda o site.",
    "5. Processamento: O servidor recebe o pedido e procura os arquivos da página.",
    "6. Resposta: O servidor envia de volta os arquivos de texto, imagens e códigos (HTML/CSS).",
    "7. Renderização: O navegador lê esses códigos e desenha a página visual na sua tela."
]

print("--- COMO ACESSAR UM SITE (DETALHADO) ---")
for passo in passos_detalhados:
    print(passo)
