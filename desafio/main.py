emails = "joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br, rodrigo.lima@alun.com.br, artur.rosa@alun.com.br"

emails_separados = emails.replace(" ", "").split(",")

usuarios_por_dominio = {}

def trocar_primeiro_ultimo(lista: list) -> list:
    lista[0], lista[-1] = lista[-1], lista[0]
    
    return lista

for email in emails_separados:
    usuario, dominio = email.split("@")
    
    if dominio not in usuarios_por_dominio:
        usuarios_por_dominio[dominio] = []
        
    usuarios_por_dominio[dominio].append(usuario)

for dominio, usuarios in usuarios_por_dominio.items():
    print("Quantidade de emails por domínio:")
    print(f"{dominio}: {len(usuarios)}")
    print(f"Lista de usuários: {tuple(usuarios)}")
    
    usuarios = trocar_primeiro_ultimo(usuarios)
    usuarios_tupla = tuple(usuarios)
    
    print(f"Após troca de posições: {usuarios_tupla}")
    print()