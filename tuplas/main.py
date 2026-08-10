# Declarando tuplas
t = 'a', 'b', 'c', 'd', 'e'
t = 'a',
t = ('a', 'b', 'c', 'd', 'e')

# Verificando tipo
print(type(t))

# Imprimindo tupla
print(t)

# Imprimindo um item específico da tupla
print(t[1])

# Imprimindo uma range de tupla
print(t[1:3])

# Criando uma nova tupla a partir de uma existente
t = ("F",) + t[1:]
print(t)

# Atribuição com tuplas
a = 5
b = 10

a, b = b, a
print(a, b)

end_email = "fulano@gmail.com"
nome_usuario, dominio = end_email.split("@")

print(f"Nome usuário: {nome_usuario} | Domínio: {dominio}")