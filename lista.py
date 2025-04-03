lista = [10, 20, 30, 40, 50,]
print(lista[2])

lista[2] = 100
print(lista)

lista.append(60)
lista.pop(0)
print(lista)

list.sort(lista)
print(lista)
lista.sort(reverse=True)
print(lista)

soma = sum(lista)

media = soma / len(lista)
print(media)