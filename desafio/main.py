def contar_dominios(emails):
    dicionario = dict()
    
    for email in emails:
        _, dominio = email.split("@")
        
        if dominio not in dicionario:
            dicionario[dominio] = 1
        else:
            dicionario[dominio] += 1
            
    return dicionario

def exibir_email_por_chave(chave, dicionario):
    if chave in dicionario:
        for email in emails_separados:
            nome_usuario, dominio = email.split("@")
            
            if dominio == chave:
                print(nome_usuario, end=", ")
                         
                
emails = "joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br, rodrigo.lima@alun.com.br"

emails_separados = emails.replace(" ", "").split(",")

dicionario = contar_dominios(emails_separados)

for chave, dados in dicionario.items():
    print("Quantidade de emails por domínio:")
    print(f"{chave}: {dados}")
    print("Lista de Usuários: ", end="")
    exibir_email_por_chave(chave, dicionario)
    print()
    print()