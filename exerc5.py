#1 ----------
idade = int(input('Digite sua idade: '))

if idade > 17:
    print('Voce é maior de idade!')
else: print('Voce é menor de idade!')

#2-----------
temp = float(input('Digite a temperatura: '))

if temp > 29:
    print('Calor!')
elif temp < 11:
    print('Frio!')
else:
    print('Agradavel!')

#3------------
aluno = input('Digite o nome do aluno: ')
nota = float(input('Digite a nota do aluno:'))

if nota > 6:
    print('Aprovado!')
else:
    print('Reprovado!')

#4-----------
numeros = []
for i in range(10):
    num = int(input(f'Digite o numero {i+1}: '))
    numeros.append(num)
soma = sum(numeros)
print(f'A soma dos numeros é: {soma}')

#5--------
idade2 = int(input('Digite sua idade: '))

if idade > 17 and idade < 26:
    print('Jovem!')
elif idade > 25 and idade < 61:
    print('Adulto!')
else:
    print('Idoso!')

#6--------------
def imprimir_nome():
    nome2 = input("Digite seu nome: ")
    print(nome2)

imprimir_nome()

#7--------------
nume = int(input('Digite um numero: '))

if nume < 0:
    print('Digite um numero positivo!')

print(f'Tabuada do {nume}: ')
for i in range(1, 11):
    print(f'{nume} x {i} = {nume * i}')

#8-------------
preco = float(input('Digite o preço: '))

descconto = preco * 0.10
precoDesconto = preco - descconto

print(f'O preço com desconto é: {precoDesconto: .2f}')

#9---------------
preeco = float(input('DVallor do produto: $ '))

if preeco < 50.00:
    print('Menor que $50.00')
elif 50.00 <= preco <= 100.00:
    print('Entre 50 e 100')
else:
    print('Maior que $100.00')

#10------------
def calculaAreaQuadrada():
    return lado * lado

lado = float(input('Digite o valor do lado: '))
area = calculaAreaQuadrada(lado)
print(area)

#11--------------
def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    diferenca = lambda x, y: abs(x - y)

    resultado = diferenca(num1, num2)

    print(f"A diferença entre o maior e o menor número é: {resultado}")

#12------------
altura = float(input('Digite sua altura: '))

if altura > 1.40:
    print('Voce pode ir!')
else:
    print('Altura minima de 1,40!')

#13-------------
def converteTemp():
    farh = float(input('Digite a temperatura: '))
    celcius = (5/9) * (farh - 32)
    print(celcius)

converteTemp()