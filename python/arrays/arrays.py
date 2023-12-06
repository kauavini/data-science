cars = ["Ford", "Volvo", "BMW"]


print(cars[0])

print(len(cars))

for i in cars:
    print(i)


# removendo itens

cars.pop(1)
cars.remove("Ford")

print(cars)

cars.append("Celta")
copiaDeCarros = cars.copy();
contagemDeCarros = cars.count("Ford");

listaAuxiliar = ["crossfox", "peagout"]

cars.extend(listaAuxiliar)
print(cars)

cars.insert(len(cars), "Kaua")

print(cars)

cars.pop(len(cars) - 1) # remove por posicao
cars.remove("crossfox") # remove por valor
cars.reverse() # reverter a lista
cars.sort() # ordenar a lista
print(cars)
