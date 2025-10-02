#111111111111111111111111111111111111111111111111111
lista = [1,2,3,4,5]
print(list(map(lambda num:num*2, lista)))

#222222222222222222222222222222222222222222222222222
lista = [10, 15, 20, 25, 30]
print(list(filter(lambda num:num % 2 == 0, lista)))

#333333333333333333333333333333333333333333333333333
lista = [1, 2, 3, 4, 5]
print(list(map(lambda num:num + 1, lista)))

#444444444444444444444444444444444444444444444444444
frutas = ["uva", "banana", "maçã", "laranja"]
ordenadas = sorted(frutas, key=lambda x: len(x))
print(ordenadas)

#555555555555555555555555555555555555555555555555555
palavras = ["ana", "pedro", "maria"]
maiusculas = list(map(lambda x: x.capitalize(), palavras))
print(maiusculas)

#6666666666666666666666666666666666666666666666666666
from functools import reduce
numeros = [2,3,4,5]
print(reduce(lambda x, y : x * y, numeros))

#77777777777777777777777777777777777777777777777777777
lista = ["banana", "uva", "maçã", "laranja"]
ordem = sorted(lista, key=lambda x: x[-1])
print(ordem)




