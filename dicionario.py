#Adiciona biblioteca e exibe um valor
produtos = {
    'Notebook': 3500,
    'Teclado': 150,
    'Mouse': 80
}
print(produtos['Teclado'])

#Adiciona produto e modifica preço
produtos['Monito'] = 1200
produtos['Notebook'] = 4000
print(produtos)

#Delete um item
del produtos['Mouse']
print(produtos)

#Percorre e exibe por chave
for chave, valor in produtos.items():
    print(f'Produto: {chave}, Preço: R${valor}')

#Converte um dicionario em uma lista de tuplas
listaDeTuplas = list(produtos.items())
print(listaDeTuplas)