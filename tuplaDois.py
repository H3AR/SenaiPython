#6 - Mostra ultima cidade
tupla = ('Curvelo', 'Inimutaba', 'Corinto', 'BH', 'Cerro', 'Monjolos')
print(tupla[5])


#7 - Tupla para Lista
lista = list(tupla)
del lista[5]

tupla = tuple(lista)
print(tupla)

#8 - Conecta tupla
tupla2 = ('Azul', 'Verde', 'Cinza')
tupla3 = ('Rosa', 'Preto', 'Branco')

juntaTupla = tupla2 + tupla3
print(juntaTupla)

#9 - Verifica presença
tuplaCode = ('Java', 'C++', 'Python', 'TS', 'JS')
valor = 'Python'

if valor in tuplaCode:
    print(f'O valor {valor}, está presente na Tupla')
else:
    print(f'O valor {valor}, não está presente na tupla!')

#10 - Encontrar posição
tuplaNum = ('10', '20', '30', '40', '50')

valor = '50'
indice = tuplaNum.index(valor)
print(f'O valor {valor}, está na posição {indice} da tupla!')
