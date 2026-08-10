# Dicionário vazio
eng2sp = dict()
print(eng2sp)

# Dicionário com um valor
eng2sp["one"] = "uno"
print(eng2sp)

# Dicionários de números
eng2sp = {
    "one": "uno", 
    "two": "dos", 
    "three": "tres"
}

# Acessando tamanho do dicionário
print(len(eng2sp))

# Acessando posição específica
print(eng2sp["two"])

# Verificando se há uma chave no dicionário
print("one" in eng2sp)

# Verificando valores das chaves
valores_dict = eng2sp.values()
print("uno" in valores_dict)

# Contar letras de um dicionário
def contar_letras(s):
    d = dict()

    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

print(contar_letras("ovo"))