emails = "joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br, rodrigo.lima@alun.com.br"

emails_separados = emails.replace(" ", "").split(",")

def mostrar_emails(emails):
    for email in emails:
        nome_usuario, dominio = email.split("@")
        print(f"Usuário: {nome_usuario} | Domínio: {dominio}")

def contar_dominios(emails):
    dicionario = dict()
    
    for email in emails:
        _, dominio = email.split("@")
        
        if dominio not in dicionario:
            dicionario[dominio] = 1
        else:
            dicionario[dominio] += 1
            
    return dicionario

dicionario = contar_dominios(emails_separados)

for chave, dados in dicionario.items():
    print("Quantidade de emails por domínio:")
    print(f"{chave}: {dados}")
    print()