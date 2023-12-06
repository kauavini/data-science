#conjunto de dados nao ordenados

carros = {"Jetta Variant", "Passat", "Crossfox", "Dodge Journey"}

carros = {"name": "Passat", "idade": 12}
print(carros["name"])

print(type(carros))

for i in carros:
  print(i)


# listas e a função set

lista_escolas = ["Data Science", "Programação", "Frontend", "Mobile", "Inovação e Gestão"]

escolas_set = set(lista_escolas)
print(escolas_set)


# operacoes => correlacionar conjuntos
# disjuntos => nenhum elemento em comum
# união => conjuntos em comum
acessorios_passat = set(["Rodas de Liga", "Travas Elétricas", "Piloto Automático", "Central Multimídia", "Inovação e Gestão"])
acessorios_crosfox = set(["Rodas de Liga", "Travas Elétricas", "Piloto Manual", "Som Bluetooth", "Inovação e Gestão"])


print(set.isdisjoint(acessorios_crosfox, acessorios_passat))
acessorios_crosfox & acessorios_passat
print(set.intersection(acessorios_crosfox, acessorios_passat))
print(set.union(acessorios_crosfox, acessorios_passat, {"Teto Solar"}))

