emails = "joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br, rodrigo.lima@alun.com.br, artur.rosa@alun.com.br"

emails_separados = emails.replace(" ", "").split(",")

usuarios_por_dominio = {}

for email in emails_separados:
    usuario, dominio = email.split("@")
    
    if dominio not in usuarios_por_dominio:
        usuarios_por_dominio[dominio] = []
        
    usuarios_por_dominio[dominio].append(usuario)

for dominio, usuarios in usuarios_por_dominio.items():
    usuarios_tupla = tuple(usuarios)

    primeira_posicao = 0
    ultima_posicao = len(usuarios_tupla) - 1

    primeiro_usuario = usuarios_tupla[primeira_posicao]
    ultimo_usuario = usuarios_tupla[ultima_posicao]

    primeiro_usuario, ultimo_usuario = ultimo_usuario, primeiro_usuario
    
    print("Quantidade de emails por domínio:")
    print(f"{dominio}: {len(usuarios)}")
    print(f"Lista de usuários: {usuarios}")
    print(f"Após troca de posições: {primeiro_usuario}, {usuarios_tupla[1:ultima_posicao]}, {ultimo_usuario}")
    print()