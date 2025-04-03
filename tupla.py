#Cria tupla
tupla = ('Heitor', 'Araujo', 'Rubim', 'Coddy')
print(tupla[1]) #Printa indice 1 da tupla

#Passa Tupla para lista
lista = list(tupla) 
lista[1] = 'Jake' #Altera indice 1 da lista

tupla = tuple(lista) #Passa Lista para Tupla
print(tupla) #Printa Tupla

#Verifica veracidade do valor na tupla
valor = 'Jake'
if valor in tupla:
    print(f"O valor {valor}, está presenta na tupla!")
else:
    print(f"O valor {valor}, não está presente na tupla!")

#Unir tuplas
tupla2 = ('Lia', 'Elvis', 'Manuque')

tuplaUnida = (tupla + tupla2)
print(tuplaUnida)

#Index na tupla
valor = 'Jake'
indice = tupla.index(valor)

print(f"O valor {valor} está no indice {indice}!")