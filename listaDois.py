#1 - Exibir 5 valor da lista
lista = [1, 2, 3, 4, 5]
print(lista[4])

#2 - Remove numeros impares
def removeImpares(lista):
    return [x for x in lista if x % 2 == 0]

listaSemPares = removeImpares(lista)
print(listaSemPares)

#3 - Verifica se valor é verdade
lista2 = ['Pera', 'Uva', 'Banana', 'Maçã', 'Goiaba']
valor = 'Maçã'
if valor in lista2:
    print(f'O valor {valor}, esta na lista!')
else:
    print(f'O valor {valor}, não está presente na lista!')

#4 - Multiplica valor
multValores = [valor * 2 for valor in lista]
print(multValores)

#5 - Reverte valores
reverse = lista[::-1]
print(reverse)