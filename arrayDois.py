import numpy as np

#11 - Cria array numPy
array = np.array ([1, 2, 3, 4, 57, 68, 79, 8, 9, 10])
print(array)

#12 - Torrna os numeros negativos
print(array * -1)

#13 - Substitui todos numeros maiores que 50 por 50
array[array > 50] = 50

print(array)

#14 - Diferença entre arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([2, 7, 9, 4, 3])

diferenca = np.setdiff1d(array1, array2)
print(diferenca)

#15 - Maior e menor numero
numMaior = np.max(array1)
numMenor = np.min(array1)

print(numMaior)
print(numMenor)