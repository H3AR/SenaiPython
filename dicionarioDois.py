#16 - Exiibir capital Brasil
paises = {
    'Brasil': 'Brasilia',
    'Argentina': 'Bueno Aires',
    'Alemanha': 'Berlin',
    'Paraguai': 'Assunção',
    'Ucrania': 'Kiev'
}
print(paises['Brasil'])

#17 - Modifica
paises['Brasil'] = 'Salvador'
print(paises)

#18 - Adiciona pais e capital
paises['Equador'] = 'Quito'
print(paises)

#19 - Remove um pais
del paises['Alemanha']
print(paises)

#20 - Converte dicionario em duas listas
chaves = list(paises.keys())
valores = list(paises.values())

print('Chaves: ',chaves)
print('Valores: ', valores)