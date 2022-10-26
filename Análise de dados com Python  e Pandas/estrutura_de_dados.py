#PraticandoDicionários

dc = {"Maça":20, "Banana":10, "Laranja":15, "Uva":5}

print(dc)

#acessando valor do dicionário através da chave especifica
print(dc['Maça'])


#Atualizando valor de Maça
dc['Maça'] = 25

print(dc)

#Retornando todas as chaves do dicionário
print(dc.keys())

#Retornando todas os valores do dicionário
print(dc.values())

#Verificando se já existe uma chave no dicionário e caso não exista inserir
dc.setdefault('Limão',22)

print(dc)
